from flask.ext.security import current_user
from application.core.utils import get_now, get_editor
from application.extensions import db
from sqlalchemy.sql.expression import ClauseElement
from flask.ext.security import current_user
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.orm.properties import ColumnProperty
import collections


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        instance = model(**params)
        session.add(instance)
        return instance, True


class SerializableMixin(object):
    introspection_level = 1
    force_introspect = ('User', 'Role')
    skip_columns = ('modified_by', 'created_by', 'content_type', 'deleted_at',
                    'current_login_at', 'current_login_ip', 'confirmed_at',
                    'last_login_at', 'last_login_ip', 'password', 'login_count')
    add_fields = ()

    def to_dict(self, level=0):
        if level >= self.introspection_level and str(self.__class__.__name__) not in self.force_introspect:
            print "Introspection level exceeded ({} > {})".format(level, self.introspection_level)
            return {}

        mapper = class_mapper(self.__class__)

        data = {}

        for prop in mapper.iterate_properties:
            if prop.key not in self.skip_columns:
                if type(prop) == ColumnProperty:
                    value = getattr(self, prop.key)
                    data[prop.key] = value
                elif type(prop) == RelationshipProperty:
                    value = getattr(self, prop.key)
                    if isinstance(value, collections.Iterable):
                        data[prop.key] = []
                        for sub_prop in value:
                            if hasattr(sub_prop, 'to_dict'):
                                sub_value = sub_prop.to_dict(level+1)
                                if sub_value:
                                    data[prop.key].append(sub_value)
                    else:
                        data[prop.key] = value.to_dict(level+1)

        for prop in self.add_fields:
            value = getattr(self, prop, 'No')
            data[prop] = value() if hasattr(value, '__call__') else value

        return data


class ObservableMixin(object):
    created_by = db.Column(db.String(80), unique=False, nullable=False, default=get_editor)
    created_date = db.Column(db.DateTime, unique=False, nullable=False, default=get_now)
    modified_by = db.Column(db.String(80), unique=False, nullable=True, onupdate=get_editor)
    modified_date = db.Column(db.DateTime, unique=False, nullable=True, onupdate=get_now)


class SafeDeleteMixin(object):
    deleted_at = db.Column(db.DateTime)

    def safe_delete(self):
        self.deleted_at = get_now()
        self.save(validate=False)

    def undelete(self):
        if self.deleted_at:
            self.deleted_at = None
            self.save(validate=False)


class GetOnOrNoneMixin(object):
    @classmethod
    def get_one(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).first()
        except:
            return None

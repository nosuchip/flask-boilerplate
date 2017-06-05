# -*- coding: utf-8 -*-

from flask_security.datastore import Datastore, UserDatastore
from flask_security.utils import get_identity_attributes


class RawSQLADatastore(Datastore):
    def commit(self):
        self.db.commit()

    def put(self, model):
        self.db.add(model)
        self.db.commit()
        return model

    def delete(self, model):
        self.db.delete(model)


class RawSQLAUserDatastore(RawSQLADatastore, UserDatastore):
    def __init__(self, db, user_model, role_model):
        RawSQLADatastore.__init__(self, db)
        UserDatastore.__init__(self, user_model, role_model)

    def _is_numeric(self, value):
        try:
            int(value)
        except (TypeError, ValueError):
            return False
        return True

    def get_user(self, identifier):
        if self._is_numeric(identifier):
            return self.db.query(self.user_model).query.get(identifier)

        for attr in get_identity_attributes():
            query = getattr(self.user_model, attr).ilike(identifier)
            rv = self.db.query(self.user_model).filter(query).first()
            if rv is not None:
                return rv

    def find_user(self, **kwargs):
        return self.db.query(self.user_model).filter_by(**kwargs).first()

    def find_role(self, role):
        return self.db.query(self.role_model).filter_by(name=role).first()

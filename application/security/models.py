from flask import url_for
from flask.ext.security import UserMixin, RoleMixin
from application.extensions import db
from application.core.mixins import SerializableMixin, GetOnOrNoneMixin, SafeDeleteMixin
import hashlib


users_to_roles_association_table = db.Table('users_to_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))


class User(db.Model, UserMixin, SerializableMixin, GetOnOrNoneMixin, SafeDeleteMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255), unique=True)
    last_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=users_to_roles_association_table,
                            backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(16))
    current_login_ip = db.Column(db.String(16))
    login_count = db.Column(db.Integer())

    def __unicode__(self):
        return u"<User {} ({} {})>".format(self.email, self.first_name, self.last_name)

    def __repr__(self):
        return self.__unicode__()

    @property
    def display_name(self):
        if self.first_name or self.last_name:
            return ' '.join((self.first_name, self.last_name))

        return self.email

    @property
    def gravatar_link(self):
        m = hashlib.md5()
        m.update(self.email)
        return "http://www.gravatar.com/avatar/{}".format(m.hexdigest())

    @property
    def profile(self):
        return url_for('user_view.index', user_id=self.id)


class Role(db.Model, RoleMixin, SerializableMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, db.Sequence('role_id_seq'), primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(128), unique=False, nullable=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()

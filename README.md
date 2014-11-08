Flask-Boilerplate
=================

Flask application with batteries:
* Flask-Admin
* Babel
* SQLAlchemy
* Flask-Security
* Flask-Mail

###Admin

Admin module exports `init_admin` which aimed to initialize all admin-related stuff `views.py`
- `add_admin_views` which  initialize all views in admin
- admin views base `AdminModelView` provided widely used methods
- couple of administrative view which  inherits  `AdminModelView`  and  perform
admin view for specific models


###Config
Defined configuration for application. Consist of following files:
- `app.py` defines all application-related settings
- `flask.py` defines all settings required fy application's extensions
- `messages.py` defines messages and elements labels and descriptions


###Core
- `errors.py` provides basic errors infrastructure for JSON responses
- `filters.py` provides filters used in forms to cleanup data
- `mixins.py` provides application-wide mixins for models. It exports:
  - `get_or_create` method aimed to return entity or create and return it
  - `SerializableMixin` mixin performed converting model to python  `dict`  and
  following  transformation  to  JSON.  Directly  SQLAlchemy  models   is   not
  json-serializable. It allows to define introspection level to break  circular
  dependencies loop.
  - `ObservableMixin` allow track model's creator and updater and time of these
  actions.
  - `SafeDeleteMixin` adds field `deleted_at`  and  make  model  soft-deletable
  (i.e. if this field is not `None` it is means that record is deleted. It should be handled by business logic to filter such recored).
  - `GetOnOrNoneMixin` allows to take only one record or `None` if  it  is  not
  found by criterias specified.


###Security
- Module export `init_security` aimed to initialize instance of  Flask-Security
with application and specify user and role models
- `context_processors.py`  exports  `init_context_processors`  which  aimed  to
encapsulate all context processing for different events
- `forms.py` defined models used by Flask-Security
- `models.py` defines `User` and `Role` models
 required by Flask-Security


###Static
Contains default libraries and application's javascrip, CSS and assets
Library includes:
- Bootstrap v3.2.0 (http://getbootstrap.com)
- X-editable - v1.5.1 (http://github.com/vitalets/x-editable)
- Bootstrap-select v1.5.4 (http://silviomoreto.github.io/bootstrap-select/)
- HTML5 Shiv 3.7.2 for IE
- jQuery v2.1.1 (http://jquery.com/)
- Knockout (http://knockoutjs.com/)
- Lightbox v2.7.1 (http://lokeshdhakar.com/projects/lightbox2/)
- Respond.js v1.4.2 (https://github.com/scottjehl/Respond)
- Simple Line Icons (http://graphicburger.com/simple-line-icons-webfont/)

###Extensions
Exports  `configure_extensions`  method  to  configure  all  3rd  party   Flask
extensions. By default includes:
- db (database instance for querying and model defining)
- babel (translation engine)
- mail (Flask-Main instance to send emails)
- assets (webassets instance to bundle and minify you CSS and javascript before
sending to client; it allows to make 2 requests instead of, for example, 10 - one per resourse).

###Routes
Defined basic simple routes which does not requires complex context and can  be
marshallized simply with static set of variables. Of course it is externable!
Also defined route for `favicon` and 404 and 500 errors

###Main
Initialize  application,  extensions,  setting  up  blueprints  for  views  and
services and exports originl application as `app`

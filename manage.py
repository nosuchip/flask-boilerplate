# manage.py

from flask_script import Manager

from application import flask_app

manager = Manager(flask_app)

if __name__ == "__main__":
    manager.run()
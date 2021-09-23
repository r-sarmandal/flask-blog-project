from flask.cli import with_appcontext

from flaskblog import db

@with_appcontext
def create_tables():
    db.create_all()

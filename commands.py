from flask.cli import with_appcontext
import click
from flaskblog import db
from flaskblog.models import User, Post

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

import cmd
from flaskblog import db
from flask import Blueprint

cmd = Blueprint('db', __name__)
@cmd.cli.command('create_db')
def createDatabase():
    db.create_all()

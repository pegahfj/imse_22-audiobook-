import sys

from src import create_app, db
from flask.cli import FlaskGroup


app = create_app()  
cli = FlaskGroup(create_app=create_app)  


@cli.command('initdb')
def initdb():
    db.init_db()


if __name__ == '__main__':
    cli()
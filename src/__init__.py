import os

from flask import Flask
from flask_bcrypt import Bcrypt
import psycopg2
from .RDBMS.db_manager import MyDB


# bcrypt = Bcrypt(app)

# db
connection = psycopg2.connect(user="postgres", password="postgres", host="api-db", port="5432", database="postgres_db")
db = MyDB(connection)



def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__, template_folder='templates')

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    
    # set up extensions
    db.init_app(app)

    # register blueprints
        
    from src.routes import index
    app.register_blueprint(index)

    from src.routes import register
    app.register_blueprint(register)

    from src.routes import login
    app.register_blueprint(login)

    from src.routes import new_book_author
    app.register_blueprint(new_book_author)

    from src.routes import new_book
    app.register_blueprint(new_book)

    from src.routes import search
    app.register_blueprint(search)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
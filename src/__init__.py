import os

from flask import Flask
from flask_bcrypt import Bcrypt
import psycopg2
from .api.rdbms.db_manager import MyDB



# db
connection = psycopg2.connect(user="postgres", password="postgres", host="api-db", port="5432", dbname="postgres_db")
db = MyDB(connection)

# instantiate the app
bcrypt = Bcrypt()


def create_app(script_info=None):


    app = Flask(__name__, template_folder='templates')
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    bcrypt.init_app(app)

    # register blueprints
    from .routes import index_blueprint
    app.register_blueprint(index_blueprint)

    from .routes import register_blueprint
    app.register_blueprint(register_blueprint)

    from .routes import login_blueprint
    app.register_blueprint(login_blueprint)

    from .routes import new_book_author_blueprint
    app.register_blueprint(new_book_author_blueprint)

    from .routes import new_book_blueprint
    app.register_blueprint(new_book_blueprint)

    from .routes import search_blueprint
    app.register_blueprint(search_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
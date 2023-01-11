import os

from flask import Flask
from flask_bcrypt import Bcrypt
import psycopg2
from flask_login import LoginManager


from .api.rdbms.db_manager import MyDB



# db
connection = psycopg2.connect(user="postgres", password="postgres", host="api-db", port="5432", dbname="postgres_db")
db = MyDB(connection)

# instantiate the app
bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = "login"
# login_manager.login_message_category = "info"

def create_app(script_info=None):

    app = Flask(__name__, template_folder='templates')
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # login_manager.init_app(app)
    bcrypt.init_app(app)


    # register blueprints
    from .api.rdbms.main.routes import index
    app.register_blueprint(index)

    from .api.rdbms.users.routes import users
    app.register_blueprint(users)
    
    from .api.rdbms.books.routes import book
    app.register_blueprint(book)

    # with app.app_context():
    #     login_manager.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
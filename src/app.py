from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_bcrypt import Bcrypt
import psycopg2
from .RDBMS.db_manager import MyDB


app = Flask(__name__, template_folder='templates')

app.config.from_object('src.config.DevelopmentConfig') 
bcrypt = Bcrypt(app)
#  db
connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres_db")
db = MyDB(connection)

def create_and_fill_db():
    db.init_db()
    

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

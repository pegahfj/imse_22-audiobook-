from .forms import SearchForm
# from .app import db,bcrypt 
from src import db

from flask import Blueprint, url_for, render_template, flash, redirect
from functools import wraps


index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    search = form.search.data
    
    if search:
        return search_res()
    else:
        books = db.get_all_books()
        return render_template('home.html', posts=books, form=form)


@index.route('/search', methods=['GET', 'POST'])
def search_res():
    form = SearchForm()
    search = form.search.data
    # flash(f'Showing Search Results for {search} ', 'success')
    book = db.search_books(search)
    return render_template('search.html', results=book, form=form)


@index.route('/fillingDB') 
def fillingDB(): 
    db.insert_bookCsv()
    return redirect(url_for('index.home'))


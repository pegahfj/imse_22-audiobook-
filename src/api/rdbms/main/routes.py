from .forms import SearchForm
# from .app import db,bcrypt 
from src import db

from flask import Blueprint, url_for, render_template, flash, redirect
from functools import wraps
# from flask_login import current_user, login_required

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    search = form.search.data
    # search = musicsearchform(request.form)
    # if request.method == 'post':
    #     return search_results(search)
    if search:
        return search_res()
    books = db.get_all_books()
    return render_template('home.html', posts=books, form=form)

@index.route('/search', methods=['GET', 'POST'])
def search_res():
    form = SearchForm()
    search = form.search.data
    # flash(f'Showing Search Results for {search} ', 'success')
    book = db.search_books(search)
    return render_template('search.html', results=book, form=form)



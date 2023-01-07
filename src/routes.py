from .forms import User_register, User_login, New_book_author, New_book, SearchForm
# from .app import db,bcrypt 
from src import db, bcrypt 

from flask import Blueprint, url_for, render_template, flash, redirect, request, session, make_response
from functools import wraps

index_blueprint = Blueprint('index', __name__)
register_blueprint = Blueprint('register', __name__)
login_blueprint = Blueprint('login', __name__)
logout_blueprint = Blueprint('logout', __name__)
new_book_author_blueprint = Blueprint('new_book_author', __name__)
new_book_blueprint = Blueprint('new_book', __name__)
search_blueprint = Blueprint('search', __name__)



@index_blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    search = form.search.data
    # search = musicsearchform(request.form)
    # if request.method == 'post':
    #     return search_results(search)
    if search:
        return search_res()
    books = db.get_books()
    return render_template('home.html', posts=books, form=form)


@register_blueprint.route('/register', methods=['GET', 'POST'])
def user_register():
    form = User_register()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.insert_user(form.username.data, form.email.data, hashed_password)
        flash(f'Account Created Successfully!', 'success')
        return redirect(url_for('index.home'))
    return render_template('register.html', title='Register', form=form)


@login_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    form = User_login()
    if request.method == 'POST':
        if form.validate_on_submit():
            exist_email = db.validate_email(form.email.data)
            if exist_email:
                user:list = db.get_user(form.email.data)
                if bcrypt.check_password_hash(user[3], form.password.data):
                    session['logged_in'] = True
                    session['username'] = user[1]
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('index.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login.user_login'))
    return wrap

# Logout
@logout_blueprint.route('/logout')
@is_logged_in
def user_logout():
    session.clear()
    session.Abandon()
    flash('You are now logged out', 'success')
    return render_template('login.html', title='Login')

# 1 find the email 
# 2 check passworde


@new_book_author_blueprint.route('/new_book_author', methods=['GET', 'POST'])
def add_book_author():
    form = New_book_author()
    if form.validate_on_submit():
        auth = db.find_author(form.auth_name.data)
        if auth:
            flash('Similar Author seem to exist already', 'danger')
            return redirect(url_for('new_book.add_book'))
        else:
            book = db.search_by_book(form.title.data)
            if book:
                flash('Similar Book seem to exist already', 'danger')
                return redirect(url_for('index.home'))
            else: 
                db.insert_book_author(form.auth_name.data, form.country.data, form.title.data, form.year.data, form.language.data)
                flash(f'Audiobook Was Added Successfully!', 'success')
                return redirect(url_for('index.home'))
    return render_template('new_book_author.html', title='new_book_author', form=form)


@new_book_blueprint.route('/new_book', methods=['GET', 'POST'])
def add_book():
    form = New_book()
    form.auth_name.choices = [(row[0], row[1]) for row in db.get_authors()]
    if form.validate_on_submit():
        book = db.search_by_book(form.title.data)
        if book:
            flash('Similar Book seem to exist already', 'danger')
            return redirect(url_for('index.home'))
        else:
            db.insert_book(form.auth_name.data, form.title.data, form.year.data, form.language.data)
            flash(f'Audiobook Was Added Successfully!', 'success')
            return redirect(url_for('index.home'))
    return render_template('new_book.html', title='new_book', form=form)

@search_blueprint.route('/search', methods=['GET', 'POST'])
def search_res():
    form = SearchForm()
    search = form.search.data
    # flash(f'Showing Search Results for {search} ', 'success')
    book = db.search_books(search)
    return render_template('search.html', results=book, form=form)
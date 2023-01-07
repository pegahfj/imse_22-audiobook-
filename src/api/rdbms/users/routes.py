from .forms import User_register, User_login, New_book_author, New_book, SearchForm
# from .app import db,bcrypt 
from src import db, bcrypt 

from flask import Blueprint, url_for, render_template, flash, redirect, request, session, make_response
from functools import wraps

users = Blueprint('users', __name__)

register_blueprint = Blueprint('register', __name__)
login_blueprint = Blueprint('login', __name__)
logout_blueprint = Blueprint('logout', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = User_register()
    if form.validate_on_submit():
        exist_email = db.validate_email(form.email.data)
        if not exist_email:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            db.insert_user(form.username.data, form.email.data, hashed_password)
            flash(f'Account Created Successfully!', 'success')
        else:    
            flash(f'Email already exists!', 'danger')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = User_login()
    if request.method == 'POST':
        if form.validate_on_submit():
            exist_email = db.validate_email(form.email.data)
            if exist_email:
                user:list = db.get_user(form.email.data)
                if bcrypt.check_password_hash(user[3], form.password.data):
                    # session['logged_in'] = True
                    # session['username'] = user[1]
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('index.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# Check if user logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, Please login', 'danger')
#             return redirect(url_for('login.user_login'))
#     return wrap

# Logout
# @logout_blueprint.route('/logout')
# @is_logged_in
# def user_logout():
#     session.clear()
#     session.Abandon()
#     flash('You are now logged out', 'success')
#     return render_template('login.html', title='Login')

# 1 find the email 
# 2 check passworde





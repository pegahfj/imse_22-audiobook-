from flask import Blueprint, url_for, render_template, flash, redirect, request, session, make_response
from functools import wraps
# from flask_login import login_user, current_user, logout_user, login_required


from .forms import User_register, User_login
# from .app import db,bcrypt 
from src import bcrypt
from .user_model import User, UserCollection



users = Blueprint('users', __name__)



@users.route('/register', methods=['GET', 'POST'])
def register():
    form = User_register()
    
    if form.validate_on_submit():
        exist_email = User.validate_email(form.email.data)
        if not exist_email:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            id = User.insert(form.username.data, form.email.data, hashed_password)
            flash(f'Account Created Successfully! ID:{id}', 'success')
        else:    
            flash(f'Email already exists!', 'danger')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = User_login()
   
    if request.method == 'POST':
        if form.validate_on_submit():
            exist_email = User.validate_email(form.email.data)
            if exist_email:
                user:User = User.get_byEmail(form.email.data)
                if bcrypt.check_password_hash(user.password, form.password.data):
                    session['logged_in'] = True
                    session['user_id'] = user.id
                    session['username'] = user.username
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
            return redirect(url_for('users.login'))
    return wrap


# Logout
@users.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index.home'))


################ COLLECTION ###################

@users.route("/user/collection")
@is_logged_in
def collection():
    colct = UserCollection(session['user_id'])
    books = colct.get_books()
    return render_template('collection.html', books=books)

@users.route('/collection/<id>/add', methods=['POST'])
@is_logged_in
def add_toCollect(id):
    colct = UserCollection(session['user_id'])  
    colct.add_book(id)
    return redirect(url_for('users.collection'))





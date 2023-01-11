from .forms import  New_book_author, New_book
# from .app import db,bcrypt 
from src import db, bcrypt 

from flask import Blueprint, url_for, render_template, flash, redirect, request, session, make_response
from functools import wraps
# from flask_login import current_user, login_required

book = Blueprint('book', __name__)



@book.route('/new_book_author', methods=['GET', 'POST'])
def add_book_author():
    form = New_book_author()
    if form.validate_on_submit():
        auth = db.get_author_byName(form.auth_name.data)
        if auth:
            flash('Similar Author seem to exist already', 'danger')
            return redirect(url_for('book.add_book'))
        else:
            book = db.search_by_book(form.title.data)
            if book:
                flash('Similar Book seem to exist already', 'danger')
                return redirect(url_for('index.home'))
            else: 
                db.insert_book_withAuthor(form.auth_name.data, form.country.data, form.title.data, form.year.data, form.language.data)
                flash(f'Audiobook Was Added Successfully!', 'success')
                return redirect(url_for('index.home'))
    return render_template('new_book_author.html', title='new_book_author', form=form)


@book.route('/new_book', methods=['GET', 'POST'])
def add_book():
    form = New_book()
    form.auth_name.choices = [(row[0], row[1]) for row in db.get_all_authors()]
    if form.validate_on_submit():
        book = db.search_by_book(form.title.data)
        if book:
            flash('Similar Book seem to exist already', 'danger')
            return redirect(url_for('index.home'))
        else:
            db.insert_single_book(form.auth_name.data, form.title.data, form.year.data, form.language.data)
            flash(f'Audiobook Was Added Successfully!', 'success')
            return redirect(url_for('index.home'))
    return render_template('new_book.html', title='new_book', form=form)

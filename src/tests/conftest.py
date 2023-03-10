# src/tests/conftest.py

import pytest

from src import create_app, db
from src.api.rdbms.users.User import User


@pytest.fixture(scope='module')
def test_app():
    app = create_app()  
    # app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.init_db()
    yield db  
    db.clear_db()


# @pytest.fixture(scope='function')
# def add_user():
#     def _add_user(username, email, password):
#         user = User(username, email, password)
#         user.insert()
#         return user
#     return _add_user
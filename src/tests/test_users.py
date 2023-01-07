# src/tests/test_users.py


import json
from src.api.rdbms import User

def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/register',
        data=json.dumps({
            'email': 'michael@testdriven.io',
            'password': 'michael'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'michael@testdriven.io was added!' in data['message']
    
# def test_add_user_invalid_json(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         '/users',
#         data=json.dumps({}),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Input payload validation failed' in data['message']


# def test_add_user_invalid_json_keys(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         '/users',
#         data=json.dumps({"email": "john@testdriven.io"}),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Input payload validation failed' in data['message']


# def test_add_user_duplicate_email(test_app, test_database):
#     client = test_app.test_client()
#     client.post(
#         '/users',
#         data=json.dumps({
#             'email': 'michael@testdriven.io',
#             'password': 'michael'
#         }),
#         content_type='application/json',
#     )
#     resp = client.post(
#         '/users',
#         data=json.dumps({
#             'email': 'michael@testdriven.io',
#             'password': 'michael'
#         }),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Sorry. That email already exists.' in data['message']

# def test_single_user(test_app, test_database, add_user):
#     user = add_user('jeffrey@testdriven.io', 'jeffrey')
#     client = test_app.test_client()
#     resp = client.get(f'/users/{user.id}')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert 'jeffrey@testdriven.io' in data['email']
#     assert 'jeffrey' in data['password']

# def test_all_users(test_app, test_database, add_user):
#     test_database.session.query(User).delete()  
#     add_user('michael@mherman.org', 'michael')
#     add_user('fletcher@notreal.com', 'fletcher')
#     client = test_app.test_client()
#     resp = client.get('/users')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert len(data) == 2
#     assert 'michael@mherman.org' in data[0]['email']
#     assert 'michael' in data[0]['password']
#     assert 'fletcher@notreal.com' in data[1]['email']
#     assert 'fletcher' in data[1]['password']

# def test_single_user_incorrect_id(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.get('/users/999')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert 'User 999 does not exist' in data['message']
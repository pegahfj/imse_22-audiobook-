# src/tests/test_users.py


import json
from src.api.rdbms.users.User import User


# def test_single_user(test_app, test_database, add_user):
#     user = add_user('jeffrey', 'jeffrey@testdriven.io', 'jeffrey')
#     data = user.get_user(email='jeffrey@testdriven.io')

#     assert data != None
#     assert data[0] != None
#     assert 'jeffrey@testdriven.io' in data[2] #email
#     assert 'jeffrey' in data[3] #password

# def test_all_users(test_app, test_database, add_user):
#     user1 = add_user('michael', 'michael@mherman.org', 'michael')
#     user2 = add_user('fletcher', 'fletcher@notreal.com', 'fletcher')
    
#     data1 = user1.get_user(email='michael@mherman.org')
#     data2 = user2.get_user(email='fletcher@notreal.com')

#     assert len(data1) != 0
#     assert 'michael@mherman.org' in data1[2]

#     assert 'fletcher@notreal.com' in data2[2]
#     assert 'fletcher' in data2[3]

# def test_single_user_incorrect_id(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.get('/users/999')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert 'User 999 does not exist' in data['message']
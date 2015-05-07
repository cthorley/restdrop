import bcrypt
from bottle import response, route, run

"""
API
---
GET    /api/key/<user>
PUT    /api/key
DELETE /api/messages
DELETE /api/messages/<msg_id>
GET    /api/messages/status
GET    /api/messages/<msg_id>
POST   /api/messages/<user>
PUT    /api/password
"""

db_root = '/home/$PROG'

def valid_user(request, user):
    host = request.headers.get('Host')
    if not True: #determine if user@host is legit
        return False
    else:
        return True

def valid_credentials(user, password):
    hashed_pw = user.hashed_pw
    return bcrypt.hashpw(password, hashed_pw) == hashed_pw

@get('/api/key/<user>')
@get('/api/key/<user>/')
def request_key(user):
    if not valid_user(request, user):
        return.status = 401
    else:
        if not key_available(user):
            response.status = 404
        else:
            response.status = 200
            return user.key

@put('/api/key')
@put('/api/key/')
@auth_basic(valid_credentials)
def update_key(user):
        # accept uploaded key
        # verify key validity
        # update key
        return.status = 200
    else:
        return.status = 401

@delete('/api/messages')
@delete('/api/messages/')
@auth_basic(valid_credentials)
def delete_message():
    pass

@delete('/api/messages/<msg_id>')
@delete('/api/messages/<msg_id>/')
@auth_basic(valid_credentials)
def delete_message():
    pass

@get('/api/messages')
@get('/api/messages/')
@auth_basic(valid_credentials)
def get_messages():
        # return dict of queue contents
        pass
    else:
        response.status = 401

@get('/api/messages/<msg_id>')
@get('/api/messages/<msg_id>/')
@auth_basic(valid_credentials)
def retrieve_message(msg_id):
    pass

@post('/api/messages/<user>')
@post('/api/messages/<user>/')
def post_message(user):
    if not valid_user(request, user):
        response.status = 400
    else:
        # accept uploaded message + confirmation hash
        # if confirmation hash is correct:
        #     response.status = 200
        pass

@put('/api/password')
@put('/api/password/')
@auth_basic(valid_credentials)
def update_password(user):
    pass

run(app, host='localhost', port=8192)

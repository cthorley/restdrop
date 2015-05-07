import bcrypt, os, sqlite3
from bottle import response, route, run

"""
API
---
GET    /key/<user>
PUT    /key
DELETE /messages
DELETE /messages/<msg_id>
GET    /messages/status
GET    /messages/<msg_id>
POST   /messages/<user>
PUT    /password
"""

db_root = '/home/restdrop/data'

def get_db_path(request):
    user    = request.auth[0]
    host    = request.headers.get('Host')
    account = user + '@' + host
    db_path = os.path.join(db_root, host, account)
    return db_path

def valid_user(request):
    db_path = get_db_path(request)
    return os.path.isfile(db_path)

def valid_credentials(user, password):
    password = request.auth[1]
    hashed_pw = # pulled from db
    return bcrypt.hashpw(password, hashed_pw) == hashed_pw

@get('/key/<user>')
@get('/key/<user>/')
def request_key(user):
    if not valid_user(request, user):
        return.status = 401
    else:
        if not key_available(user):
            response.status = 404
        else:
            response.status = 200
            return user.key

@put('/key')
@put('/key/')
@auth_basic(valid_credentials)
def update_key(user):
    db_path = get_db_path(request)
    db = sqlite3.connect(db_path)
    c = db.cursor()
    payload = (key, )
    c.execute('INSERT OR REPLACE INTO auth VALUES(key, ?)', payload)
    return.status = 200

@delete('/messages')
@delete('/messages/')
@auth_basic(valid_credentials)
def delete_message():
    pass

@delete('/messages/<msg_id>')
@delete('/messages/<msg_id>/')
@auth_basic(valid_credentials)
def delete_message():
    pass

@get('/messages')
@get('/messages/')
@auth_basic(valid_credentials)
def get_messages():
        # return dict of queue contents
        pass
    else:
        response.status = 401

@get('/messages/<msg_id>')
@get('/messages/<msg_id>/')
@auth_basic(valid_credentials)
def retrieve_message(msg_id):
    pass

@post('/messages/<user>')
@post('/messages/<user>/')
def post_message(user):
    if not valid_user(request):
        response.status = 400
    else:
        db_path = get_db_path(request)
        db = sqlite3.connect(db_path)
        c = db.cursor()
        payload = (id, value)
        c.execute('INSERT INTO messages(?) VALUES(?)', payload)
        response.status = 200

@put('/password')
@put('/password/')
@auth_basic(valid_credentials)
def update_password():
    db_path = get_db_path(request)
    db = sqlite3.connect(db_path)
    c = db.cursor()
    payload = (hash, )
    c.execute('INSERT OR REPLACE INTO auth VALUES(hash, ?)', payload)
    return.status = 200

run(app, host='localhost', port=8192)

import bcrypt, os, sqlite3
from bottle import auth_basic, delete, get, post, put, request, route, run

"""
API
---
GET    /key/<user>
PUT    /key
DELETE /messages
DELETE /messages/<msg_id>
GET    /messages
GET    /messages/<msg_id>
GET    /messages/status
POST   /messages/<user>
PUT    /password
"""

db_root = '/home/restdrop/data'

def get_db_path():
    user = request.auth[0]
    host = request.headers.get('Host')
    db_path = os.path.join(db_root, host, user)
    return db_path

def valid_user():
    db_path = get_db_path()
    if not os.path.isfile(db_path):
        abort(404, "User not found.")
        return False
    else:
        return True

def valid_credentials():
    if valid_user():
        db_path = get_db_path()
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute('SELECT * FROM Auth WHERE Id=hashed_pw')
        hashed_pw_record = c.fetchone()
        db.close()
        # extract hashed_pw from hashed_pw_record
        return bcrypt.hashpw(password, hashed_pw) == hashed_pw

@get('/key/<user>')
@get('/key/<user>/')
def get_key(user):
    if valid_user(user):
        db_path = get_db_path(request)
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute('SELECT * FROM Auth WHERE Id=key')
        key_record = c.fetchone()
        # provide key to response object
        db.close()
        Response.status = 200

@put('/key')
@put('/key/')
@auth_basic(valid_credentials)
def update_key(user):
    db_path = get_db_path(request)
    db = sqlite3.connect(db_path)
    c = db.cursor()
    payload = (key, )
    c.execute('INSERT OR REPLACE INTO Auth VALUES(key, ?)', payload)
    db.close()
    Response.status = 200

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
    if true:
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
    if valid_user():
        db_path = get_db_path()
        db = sqlite3.connect(db_path)
        c = db.cursor()
        payload = (id, message) # where does the message come from?
        c.execute('INSERT INTO Messages(?) VALUES(?)', payload)
        db.close()
        Response.status = 201

@put('/password')
@put('/password/')
@auth_basic(valid_credentials)
def update_password():
    hashed_pw = bcrypt.hashpw(request.auth[1], bcrypt.gensalt())
    db_path = get_db_path(request)
    db = sqlite3.connect(db_path)
    c = db.cursor()
    payload = (hashed_pw,)
    c.execute('INSERT OR REPLACE INTO Auth VALUES(hash, ?)', payload)
    db.close()
    Response.status = 201

run(host='localhost', port=8192, debug=True)
# bottle.run(server='bjoern')

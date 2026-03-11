from flask import g
from db_wrapper import get_connection

DATABASE = 'neri.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = get_connection(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_connection(DATABASE)
    with open('schema.sql', mode='r') as f:
        db.executescript(f.read())
    db.commit()
    db.close()
    print("Initialized the database.")

import sqlite3
from datetime import datetime

import click
from flask import current_app,g

def get_db():
    # Check if 'db' is already in 'g' (request-scoped global object)
    if 'db' not in g:
        # Create a new SQLite connection and assign to 'g.db'
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #? current_app.config is now configuration file location where data stored
        # print("current app config is-----------------", current_app.config['DATABASE'])
        
        g.db.row_factory = sqlite3.Row # ? Use sqlite3.Row to access query results like a dictionary
        # print("Row dict ",sqlite3.Row)
        # print("g.db.row_factory------------00--", g.db.row_factory)
        
    return g.db

        
def close_db(e=None):
    db = g.pop('db',None)
    
    if db is not None:
        db.close()
####################? 001 END

# ! Add the Python functions that will run these SQL commands to the db.py file:
def init_db():
    db = get_db()
    # print(db,'---------ikkkkkkkkkk')

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        # print(f.read, 'Read file')
        # print(db.executescript(f.read().decode('utf8')),'----------------------')


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    
    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
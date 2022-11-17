from werkzeug.security import generate_password_hash
from app.models import db, User

def seed_users():
    tawn = User(username = 'Tawn', email= 'tawn@aa.io', hashed_password= generate_password_hash('password'), \
                birth_month='December', birth_day=2, birth_year=1991, birth_hour=7, \
                birth_minutes=31, birth_am_pm='am', state_id=12, city='melrose')
    mishe = User(username = 'Mishe', email= 'mishe@aa.io', hashed_password= generate_password_hash('password'), \
                birth_month='December', birth_day=2, birth_year=1991, birth_hour=7, \
                birth_minutes=31, birth_am_pm='am', state_id=12, city='melrose')
    db.session.add(tawn)
    db.session.add(mishe)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()
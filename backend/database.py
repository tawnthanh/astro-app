from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import User

with app.app_context():
  # db.drop_all()
  db.create_all()

  tawn = User(username = 'Tawn', email= 'tawn@aa.io', hashed_password= 'password', \
              birth_month='December', birth_day=2. birth_year=1991, birth_hour=7, \
              birth_minutes=31, birth_am_pm='am', state_id=12, city='melrose')
  mishe = User(username = 'Mishe', email= 'mishe@aa.io', hashed_password= 'password', \
              birth_month='December', birth_day=2. birth_year=1991, birth_hour=7, \
              birth_minutes=31, birth_am_pm='am', state_id=12, city='melrose')


  db.session.add(tawn)
  db.session.add(mishe)


  db.session.commit()
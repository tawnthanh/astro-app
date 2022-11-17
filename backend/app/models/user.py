from datetime import datetime
from sqlalchemy.orm import relationship
from .db import db


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(255), nullable = False)
  birth_month = db.Column(db.String(100), nullable=False)
  birth_day = db.Column(db.Integer, nullable=False)
  birth_year = db.Column(db.Integer, nullable=False)
  birth_hour = db.Column(db.Integer, nullable=False)
  birth_minutes = db.Column(db.Integer, nullable=False)
  birth_am_pm = db.Column(db.String(2), nullable=False)
  state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
  city = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  state= relationship("State", back_populates="users")

  @property
  def password(self):
    return self.hashed_password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def to_dict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "birth_month": self.birth_month,
      "birth_day": self.birth_day, 
      "birth_year": self.birth_year,
      "birth_hour": self.birth_hour,
      "birth_minutes": self.birth_minutes,
      "birth_am_pm": self.birth_am_pm,
      "state": self.state.to_dict(),
      "city": self.city 
    }

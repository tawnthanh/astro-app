from .db import db
from sqlalchemy.orm import relationship

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(155), nullable= False, unique=True)
    abbre = db.Column(db.String(2), nullable= False, unique=True)

    users = relationship("User", back_populates="state")

    def to_dict(self):
        return {
            "id": self.id,
            "state": self.name,
            "abbr": self.abbr
        }
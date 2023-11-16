from ShuffleShackApp import db
from sqlalchemy.dialects.postgresql import BYTEA

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    user_name = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(60), unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    password = db.Column(BYTEA)
    d_o_b = db.Column(db.Date)
    nationality = db.Column(db.String(50))
    t_bookings = db.Column(db.Integer)
    no_shows = db.Column(db.Integer)
    guest_complaints = db.Column(db.Integer)
    host_complaints = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)

    def __eq__(self, other):
        return self.id == other.id
    
    def __repr__(self):
        return f'<User {self.id} {self.user_name}>'

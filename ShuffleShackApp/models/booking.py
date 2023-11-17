from ShuffleShackApp import db
from sqlalchemy.dialects.postgresql import JSONB
import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    is_real = db.Column(db.Boolean)
    time_made = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    check_in = db.Column(db.Integer)
    inclusions = db.Column(JSONB)
    guest_info = db.Column(JSONB)
    has_pets = db.Column(JSONB)
    room_info = db.Column(JSONB)
    property_info = db.Column(JSONB)
    status = db.Column(db.Text)
    seen_by_host = db.Column(db.Text)
    messages = db.Column(JSONB)
    review_ratings = db.Column(JSONB)
    review_reply = db.Column(db.Text)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'<Booking {self.id} {self.status}>'

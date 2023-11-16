from ShuffleShackApp import db
from sqlalchemy.dialects.postgresql import JSONB

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    available_days = db.Column(db.Text)
    name = db.Column(db.Text)
    floor = db.Column(db.Text)
    description = db.Column(db.Text)
    beds = db.Column(JSONB)
    max_guests = db.Column(db.Integer)
    has_bathroom = db.Column(db.Boolean)
    has_tv = db.Column(db.Boolean)
    extras = db.Column(JSONB)
    price = db.Column(db.Integer)
    premium = db.Column(db.Integer)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id', ondelete='RESTRICT'), nullable=False)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'<Room {self.id} {self.name}>'

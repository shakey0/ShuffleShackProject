from ShuffleShackApp import db
from sqlalchemy.dialects.postgresql import JSONB

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    display_image_url = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String)
    address_1 = db.Column(db.String)
    address_2 = db.Column(db.String)
    address_3 = db.Column(db.String)
    postcode = db.Column(db.String)
    phone_number = db.Column(db.String)
    name = db.Column(db.String)
    type = db.Column(db.String)
    description = db.Column(db.String)
    check_in_from = db.Column(db.Integer)
    check_in_to = db.Column(db.Integer)
    check_out = db.Column(db.Integer)
    cancel_period = db.Column(db.Integer)
    meals = db.Column(JSONB)
    min_age = db.Column(db.Integer)
    min_stay = db.Column(db.Integer)
    host_pets = db.Column(JSONB)
    guest_pets = db.Column(JSONB)
    pets_notice = db.Column(db.String)
    extras = db.Column(JSONB)
    review_data = db.Column(JSONB)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'<Property {self.id} {self.name}>'

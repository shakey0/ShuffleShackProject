from ShuffleShackApp import db

class PropertyImage(db.Model):
    __tablename__ = 'property_images'

    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id', ondelete='CASCADE'), nullable=False)
    image_url = db.Column(db.String)
    image_description = db.Column(db.String)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'<PropertyImage {self.id} {self.image_url}>'

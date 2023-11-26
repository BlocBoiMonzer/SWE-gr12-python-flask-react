from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column("firstName", db.String(50))
    lastname = db.Column("lastName", db.String(50))
    phonenumber = db.Column("phoneNumber", db.Integer)
    address = db.Column("address", db.String(100))
    email = db.Column("email", db.String(100))
    username = db.Column("username", db.String(50), unique=True, nullable=False)
    password = db.Column("password", db.String(100), nullable=False)
    bookings = db.relationship('Booking', backref='user_bookings', lazy=True)
    image_filename = db.Column(db.String(120), nullable=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref='user_bookings')
    tour = db.relationship('Tour', backref='tour_bookings')
    paid = db.Column(db.Boolean, default=False)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)

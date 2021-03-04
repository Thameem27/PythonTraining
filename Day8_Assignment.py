from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserDet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)

    def __repr__(self):
        return '<USer %r>' % self.username


class AddUser(db.Model):
    AccountId = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), unique=False, nullable=False)
    Email = db.Column(db.String(140), unique=True, nullable=False)
    MobileNumber = db.Column(db.Integer, unique=True, nullable=False)
    AccountType = db.Column(db.String(50), unique=False, nullable=False)
    InitialDeposit = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r is now Created with an Account Type of %r and an Initial Deposit of %r >' % (self.Username, self.AccountType, self.InitialDeposit)

# From Py Command Line Run the Below Commands

from Day8_Assignment import db

db.create_all() # Creates the Data Base Objects

from Day8_Assignment import AddUser

# Create Objects
Thameem = AddUser(Username="Thameem Mohammed",Email="Tham@yahoo.in",MobileNumber=987632145,AccountType="Savings",InitialDeposit=5000)
James = AddUser(Username="James Vincent",Email="James@yahoo.co.in",MobileNumber=987638795,AccountType="Current",InitialDeposit=10000)
Rose = AddUser(Username="Rose Vinslet",Email="Rose@reddit.in",MobileNumber=997632365,AccountType="Joint",InitialDeposit=50000)

# Add These objects to DB
db.session.add(Thameem)
db.session.add(James)
db.session.add(Rose)
db.commit()

# Query All Objects
AddUser.query.all()

# Query a Specific Record
AddUser.query.filter(AddUser.Username == "Thameem Mohammed").first()
AddUser.query.filter(AddUser.AccountType == "Current").first()
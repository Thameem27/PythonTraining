from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_restful import Api, Resource
from marshmallow import fields
from marshmallow.validate import Range, Length
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from functools import wraps
import jwt
import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MovieDataBase.sqlite3'
app.config['SECRET_KEY'] = "THAMKEY27"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class MovieDet(db.Model):
    Movie_id = db.Column(db.Integer, primary_key=True)
    Movie_Name = db.Column(db.String(100), unique=True, nullable=False)
    Genre = db.Column(db.String(40), unique=False, nullable=False)
    Language = db.Column(db.String(100), unique=False, nullable=False)
    Director = db.Column(db.String(200), unique=False, nullable=False)
    
    def __repr__(self):
        return 'Movie %r is now Create in the Database' % self.Movie_Name

class UserDet(db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), unique=True, nullable=False)
    Email = db.Column(db.String(140), unique=True, nullable=False)
    
    
    def __init__(self, Username, Password, Email):
        self.Username = Username
        self.Password = Password
        self.Email = Email
    def __repr__(self):
        return '<User %r is Created>' % self.Username


class AddReview(db.Model):
    ReviewId = db.Column(db.Integer, primary_key=True)
    User_Review = db.Column(db.String(200), unique=False, nullable=False)
    User_id = db.Column(db.Integer, nullable=False)
    Movie_id = db.Column(db.Integer, unique=False, nullable=False)
    Rating = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Review is now Inserted with a Rating of %r by  >' % (self.Rating)


class UserSchema(ma.SQLAlchemySchema):
    Username = fields.Str(required=True, validate=Length(min=4, max=16))
    Password = fields.Str(required=True, validate=Length(min=4, max=16))
    Email = fields.Str(required=False)
    class Meta:
        fields = ("Username", "Password", "Email")

User_Schema = UserSchema()
Users_Schema = UserSchema(many = True)

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MovieDet

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddReview

class ViewMovieSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MovieDet
    Movie_Name=auto_field()
    Language=auto_field()
    Genre=auto_field()
    Director=auto_field()

Movie_Schema = MovieSchema()
Review_Schema = ReviewSchema()
def token_check(f):
    @wraps(f)

    def wrapper(*args, **kwargs):
        token = None
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
        if not token:
            return "This Token is Invalid"
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = "HS256")
            current_user = UserDet.query.filter_by(User_id = data['public_id']).first()
            print(data)
            print(current_user)
        except:
            return "This Token is Invalid"
        return f(current_user, *args, *kwargs)

    return wrapper        

class Register(Resource):
    def post(self):
        data_errors = User_Schema.validate(request.json)
        if data_errors:
            abort(400, str(data_errors))
        usercheck = UserDet.query.filter_by(Username = request.json['Username']).first()
        if usercheck is not None:
            abort(400, f"{usercheck.Username} Exists in the Database")
        newuser = UserDet(Username=request.json['Username'],
                            Password=generate_password_hash(request.json['Password'], method='sha256'),
                            Email = request.json['Email']
                            )
        db.session.add(newuser)
        db.session.commit()
        return f"{newuser.Username} Created Successfully"

class Login(Resource):
    def post(self):
        auth = request.authorization
        newuser = UserDet.query.filter_by(Username = auth.username).first()
        print(newuser)
        if newuser is None:
            return "No Such User"

        print(newuser.Password, auth.password)
        if check_password_hash(newuser.Password, auth.password):
            token = jwt.encode({'public_id':newuser.User_id, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return token        
        return "Not Verified", 401


@token_check
def get_current_user_id(current_user):
    newuser = UserDet.query.filter_by(Username = current_user.Username).first()
    return newuser


class View(Resource):
    def get(self):
        newuser = get_current_user_id()
        return User_Schema.jsonify(newuser)


class AddMovie(Resource):
    @token_check
    def post(self):
        input_err = Movie_Schema.validate(request.json)
        if input_err:
            abort(400, str(input_err))
        moviecheck = MovieDet.query.filter_by(Moviename = request.json['name']).first()
        if moviecheck is not None:
            abort(400, f"{moviecheck.name} Exists in the Database")
        newmov = MovieDet(Moviename=request.json['name'],
                          Language = request.json['language'],
                          Genre = request.json['genre'],
                          Director = request.json['director'],
                         )
        db.session.add(newmov)
        db.session.commit()
        return f"{newmov.name} Created Successfully"

class AddMovieReview(Resource):
    @token_check
    def post(self):
        input_err = Review_Schema.validate(request.json)
        if input_err:
            abort(400, str(input_err))
        else:
            newrev = AddReview(Movie_id=request.json['movieid'],
                               User_Review = request.json['review'],
                               User_id = request.json['userid'],
                               Rating = request.json['rating'],
                               )
        db.session.add(newrev)
        db.session.commit()
        return f"{newrev.name} Inserted Successfully"
        
api.add_resource(Register,"/user/register")
api.add_resource(Login,"/user/login")
api.add_resource(View,"/user/view")
api.add_resource(AddMovie,"/addmovie")
api.add_resource(AddMovieReview,"/addreview")
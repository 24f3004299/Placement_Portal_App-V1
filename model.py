from flask_sqlalchemy import SQLAlchemy
#from app import create
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
#app=create()
database = SQLAlchemy()
class Role(database.Model):
    __tablename__ = 'Role'
    role_id = database.Column(database.Integer, primary_key=True)
    role_name = database.Column(database.String, unique=True)
    users = database.Relationship(
        'User', lazy='dynamic', backref='role', cascade='all,delete-orphan')
class User(database.Model, UserMixin):
    __tablename__ = 'User'
    user_id = database.Column(database.Integer, primary_key=True)
    User_email_id = database.Column(
        database.String, unique=True, nullable=False)
    user_password = database.Column(database.String, unique=False)
    role_id = database.Column(
        database.Integer, database.ForeignKey(Role.role_id))
    company = database.Relationship(
        'Company', lazy='dynamic', backref='User', cascade='all,delete-orphan')
    student = database.Relationship(
        'Student', lazy='dynamic', backref='User', cascade='all,delete-orphan')
    def get_id(self):
        return str(self.user_id)

class Student(database.Model):
    __tablename__ = 'Student'
    student_id = database.Column(database.Integer, primary_key=True)
    User_id = database.Column(database.Integer, database.ForeignKey(User.user_id), unique=False)
    Nationality= database.Column(database.String, unique=False)
    state=database.Column(database.String, unique=False)
    location= database.Column(database.String, unique=False)
    Dob= database.Column(database.Date, unique=False)   
    resume = database.Column(database.String, unique=True)
    Higher_qualification = database.Column(database.String, unique=False)
    contact=database.Column(database.Integer, unique=True)

class Company(database.Model):
    __tablename__ = 'Company'
    company_id = database.Column(database.Integer, primary_key=True)
    User_id = database.Column(
        database.Integer, database.ForeignKey(User.user_id), unique=False)
    Name = database.Column(database.String, unique=True)
    Location = database.Column(database.String, unique=False)
    about = database.Column(database.String, unique=True)
    website = database.Column(database.String, unique=True)
    drives = database.Relationship('Drive', lazy='dynamic', backref='Company', cascade='all,delete-orphan')
    status = database.Column(database.String, default="pending")
    contact = database.Column(database.Integer, unique=True)
class Drive(database.Model):
    __tablename__ = 'Drive'
    drive_id = database.Column(database.Integer, primary_key=True)
    drive_name = database.Column(database.String, unique=True)
    skill= database.Column(
        database.String, unique=False)
    typeof=database.Column(
        database.String, unique=False)

    eligibility = database.Column(database.String)
    experience = database.Column(database.String)
    application = database.Relationship(
        'Application', lazy='dynamic', backref='Drive', cascade='all,delete-orphan')
    company = database.Column(
        database.Integer, database.ForeignKey(Company.company_id), unique=False)
    status= database.Column(database.String, default="pending")
class Application(database.Model):
    __tablename__ = 'Application'
    application_id = database.Column(database.Integer, primary_key=True)
    drive_id = database.Column(
        database.Integer, database.ForeignKey(Drive.drive_id), unique=False)
    student_id = database.Column(
        database.Integer, database.ForeignKey(Student.student_id), unique=False)
    status= database.Column(database.String, default="applied")

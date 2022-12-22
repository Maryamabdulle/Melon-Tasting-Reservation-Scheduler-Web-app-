"""Database for Melon tasting Reservation Scheduler app"""
 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import flask 
db= SQLAlchemy()
 
#User class

class User (db.Model):
   """User information"""
 
   __tablename__= "users"
 
   user_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
   first_name=db.Column(db.String,nullable=False)
   last_name=db.Column(db.String, nullable=False)
   email = db.Column(db.String, nullable=False, unique=True)
   password=db.Column(db.String, nullable=False)


   reservations= db.relationship("Reservation", back_populates= "user")
 
   def __rep__(self):
       """Display user on the screen"""
 
       return f"User user_id={self.user_id} email= {self.email}>"
 
 
#Reservation class
 
class Reservation(db.Model):
   """Reservation infromation"""
 
   __tablename__ ="reservation"
   
   reservation_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
   reservation_date= db.Column(db.DateTime, unique=True, nullable=False)
   user_id= db.Column(db.Integer, db.ForeignKey("user.user_id"))
   tasting_id=db.Column(db.Integer, db.ForeignKey("tastings.tasting_id"))


   #Foreign keys for the reservation table  
   user=db.relationship("User", back_populates="reservations")


   tasting=db.relationship("Tasting", back_populates= "reservations")
 
 
   def __repr__(self):
    """Display a reservation on the screen"""
   
    return f"<Reservation reservation_id={self.reservation_id} user_id={self.user_id} data={self.date} start={self.start}>"
 
 
class Melon(db.Model):
   

   __tablename__ ="melons"


   melon_id=db.Column(db.Integer, primary_key=True, autoincrement= True)
   melon_name= db. Column(db.String, unique=True, nullable=False)
   melon_cost=db.Column(db.Integer, nullable=False)
   melon_picture=db. Column(db.String, unique=True, nullable=True)



   tastings=db.relationship("Tasting", back_populates= "melons")


   def __repr__(self):
      return f"<Melon melon_id={self.melon_id}>"



class Tasting(db.Model):
   __tablename__ ="tasting"
   tasting_id=db.Column(db.Integer, primary_key=True, autoincrement= True)
   tasting_name= db. Column(db.String, unique=True, nullable=False)
   tasting_picture=db. Column(db.String, nullable=False)
   melon_id=db.Column(db.Integer, db.ForeignKey("melons.melon_id"))


   #foreign keys used by tastings table 
   melon= db.relationship("Melon", back_populates = "tasting")


   #tables using tastings table as foreign key
   reservations=db.relationship("Reservation", back_populates= "tastings")


   def __repr__(self):
      return f"<Tasting tasting_id={self.tasting_id} tasting_name={self.tasting_name}>"




#Connect to database

def connect_to_db(flask_app, db_uri="postgresql:///melon_reservations", echo=True):
   flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
   flask_app.config["SQLALCHEMY_ECHO"] = echo
   flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
   db.app = flask_app
   db.init_app(flask_app)
 
   # print ("Connected to the db!")
 




if __name__ =="__man__":
   from server import app
 
   connect_to_db
 


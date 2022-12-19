"""Database for Melon testing Reservation Scheduler app"""
 
from flask_sqlalchemy import SQLAlchemy
 
db= SQLAlchemy()
 
#User class
class User (db.Model):
   """User information"""
 
   __tablename__= "users"
 
   user_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
   email = db.Column(db.String, nullable=False, unique=True)
   name = db.Column(db.String)
 
   reservations= db.relationship("Reservation", back_populates= "user")
 
   def __rep__(self):
       """Display user on the scree"""
 
       return f"<user_id={self.user_id} name= {self.name}>"
 
 
#Reservation class
 
class Reservation(db.Model):
   """Reservation infromation"""
 
   __tablename__ ="reservation"
   
   
   reservation_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
   date= db.Column(db.Date, nullable=False)
   start= db.Column(db.Time, nullable= False)
   end= db.Column(db.Time, nullable= False)
   user_ud= db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
 
   user=db.relationship("User", back_populates="reservations")
 
 
   def __repr__(self):
    """Display a reservation on the screen"""
 
 
    return f"<Reservation reservation_id={self.reservation_id} user_id={self.user_id} data={self.date} start={self.start}>"
 
 
#Connect to database
 
def connect_to_db (flask_app, db_uri="postgresql:///melom_reservations",echo=True):
   flask_app.config["SQLALCHEMY_DATABASE_URL"]= db_uri
   flask_app.config["SQLALCHEMY_ECHO"]= echo
   flask_app.config["SQLALCHEMY_TRACK_MODIFCATIONS"]= False
 
   db.app = flask_app
   db.init_app(flask_app)
 
   print ("Connected to the db!")
 
if __name__ =="__man__":
   from server import app
 
   connect_to_db
 


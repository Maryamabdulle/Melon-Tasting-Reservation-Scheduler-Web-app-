"""Server for melon testing reservation scheduler apps"""
 
from flask import (Flask, render_template, request, redirect, flash, session)
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import datetime, date
 
import crud
import os

# Flask app config 

app= Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined= StrictUndefined


# Homepage route to show login form


@app.route("/")
def homepage():
    """Show homepage with log in form"""

    #if user hasn't logged in, show the login form
    if "user_id" in session:
        return render_template("search.html", today=date.today())


    return render_template("homepage.html")


#User logs in, show search page
@app.route("/login", methods=["POST"])
def login():
    """Process user's log in information and show search page"""

    #Get infro from the log in form
    email= request.form.get("email")
    #Find user of the input email from database
    user= crud.get_user_by_email(email)
    #Check if user exists in database, if yes, log in by saving user_id in session

    if user: 
        session[ "user_id"] = user.user_id
        flash("You are logged in.")
        return render_template("search.html", today= date.today())


    flash("Email does not exist in database. Please try again.")
    return redirect("/")




if __name__=="__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
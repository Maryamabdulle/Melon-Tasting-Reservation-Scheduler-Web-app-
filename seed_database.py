"""Seed database"""

import os
import json
from random import choice, sample, choices
from datetime import datebase, date, timedelta



import crud
import model
import server



os.system("dropdb melon_reservations")
os.system("createdb melon_reservations")
model.connect_to_db(server.app)
model.db.create_all()




# Creating and seeding users


with open("date/users.json") as f:
    user_data= json.loads(f.read())

for user in user_data:
    user_data= json.loads(f.read())

for user in user_data:
    name=user["name"]
    email= user["email"]

    user_in_db=crud.create_user(name, email)
    model.db.session.add(user_in_db)

#Creating melons for the database

with open("date/melons.json") as f:
    melons_data= json.loads(f.read())

for melon in melons_data:
    melon_name=melon["melon_name"]
    melon_cost=melon["melon_cost"]
    melon_picture=melon["melon_picture"]

    db_melon=crud.create_melon(melon_name,melon_cost,melon_picture)
    melons_in_db.append(db.melon)

model.db.db.session.add_all(melons_in_db)


#Creating tastings for database
tasting_in_db=[]

with open("date/tastings.json") as f:
    melons_data= json.loads(f.read())

for tasting in tastings_data:
    tasting_name= tasting["tasting_name"]
    tasting_picture= tasting["tasting_picture"]

    db_tasting=crud.create_tasting(tasting_name,tasting_picture)
    tastings_in_db.append(db_tasting)


model.db.session.add_all(tastings_in_db)

model.db.session.commit()
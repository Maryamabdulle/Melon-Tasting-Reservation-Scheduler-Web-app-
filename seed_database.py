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



# Create seed users


with open("date/users.json") as f:
    user_data= json.loads(f.read())

for user in user_data
"""Script to seed database."""
from faker import Faker
import os
import json

import crud
import model
import server

os.system("dropdb melontasting")
os.system("createdb melontasting")

model.connect_to_db(server.app)
model.db.create_all()

users_in_db = []
fake = Faker()

for i in range(5):
    name=fake.name()
    email=fake.email()
    password="1234"
    new_user=crud.create_user(name, email, password)
    users_in_db.append(new_user)

print("******************************")
print(users_in_db)
print("******************************")





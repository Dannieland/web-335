# taplin_usersp2.py
# Danielle Taplin
# 9/22/23
# code for mongodb updates

#import MongoClient
from pymongo import MongoClient

#import date and time
from datetime import datetime

#import connection string for mongodb
client = MongoClient("mongodb+srv://web335_user:s3cret@web335db.y00tdmc.mongodb.net/?retryWrites=true&w=majority")

#configure access to database
db = client["web335DB"]

#create composer object to store in database
new_comp = {"firstName": "Wendy", "lastName": "Lane", "employeeId": "1301", "email": "we.lane@mail.com", "dateCreated": datetime.now()}

#insert new composer into database
db.users.insert_one(new_comp)

#output new composer data showing it was added to database
print(db.users.find_one({"lastName": 'Lane'}))

#output empty line to console
print("")

#update email address of new composer
db.users.update_one({"firstName":"Wendy"},{"$set":{"email":"wendylane@mail.com"}})

#output new composer data showing email address was updated
print(db.users.find_one({"lastName": 'Lane'}))

#output empty line to console
print("")

#delete new composer data from database
db.users.delete_one({'firstName':'Wendy'})

#attempt-print new composer data to show deletion 
print(db.users.find_one({"lastName": 'Lane'}))
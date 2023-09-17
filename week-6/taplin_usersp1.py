# taplin_usersp1.py
# Danielle Taplin
# 9/16/23
# pymongo config

#import MongoClient
from pymongo import MongoClient

#import connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@web335db.y00tdmc.mongodb.net/?retryWrites=true&w=majority")

#configure a variable to access WEB335DB
db = client["web335DB"]

#write a query to store a list of users as a variable
users = (db.users.find({}))

#print all users to the console
for doc in users:
    print(doc)

#print an empty line to separate output
print(" ")

#write a query to display a document where the employee ID is 1011
print(db.users.find_one({"employeeId": '1011'}))

#write a query to display a document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))
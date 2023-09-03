/*
taplin-assignment4.2.js
Danielle Taplin
9/2/2023
queries for MongoDB Shell assignment 4.2
*/     

//write query displaying all objects stored in users collection
db.users.find()

//write query displaying user with email of jbach@me.com
db.users.find({"email": "jbach@me.com"})

//write query displaying user with last name Mozart
db.users.find({"lastName": "Mozart"})

//write query displaying user with first name Richard
db.users.find({"firstName": "Richard"})

//write query displaying user with employee Id 1010
db.users.find({"employeeId": "1010"})
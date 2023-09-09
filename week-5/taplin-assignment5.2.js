/*
taplin-assignment5.2
Danielle Taplin
9/6/23
queries for web335 assignment 5.2
 */

//insert document to composer database containing data for Franz Schubert
db.users.insertOne({"firstName": "Franz", "lastName": "Schubert", "employeeId": "1013", "email": "fschubert@me.com", "dateCreated": new Date() })

//update document containing lastName with value "Mozart" so the email is mozart@me.com
db.users.updateOne({"lastName": "Mozart"}, {$set: {"email": "mozart@me.com"}})

//find document with changed email to demonstrate the update operation was successful
db.users.find({"email": "mozart@me.com"})

//display list of documents in the collection; showing only firstName, lastName, and email fields
db.users.aggregate( [ { $project : { "_id": 0, "firstName": 1 , "lastName": 1, "email": 1 } } ] )
/*
taplin-assignment6.2.js
Danielle Taplin
9/16/23
queries for web335 assignment 6.2
 */



//display list of documents in houses collection
db.houses.find({})

//Display list of documents in students collection
db.students.find({})

//write query to add new document to students collection
db.students.insertOne({"firstName": "Ron", "lastName": "Weasley", "studentId": "s1019", "houseId": "h1007"})

//find added document to students collection to prove it was added
db.students.find({"lastName": "Weasley"})

//write query to delete added document from students collection
db.students.deleteOne({"firstName": "Ron"})

//attempt finding deleted document from students collection to prove it was deleted
db.students.find({"lastName": "Weasley"})

//write query to search for students by respective houses
db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } } ] )

//write query to search for students of house Gryffindor
db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }, 
{ $match: {"founder": "Godric Gryffindor"}} ] )

//write query to search for students in house with eagle mascot
db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }, 
{ $match: {"mascot": "Eagle"}} ] )
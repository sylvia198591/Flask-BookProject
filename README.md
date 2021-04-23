					Book Store Project

Framework: Flask Restplus
Database: MongoDB
APIs : Requests and Responses

Request Method : POST Method -  http://127.0.0.1:5000/api/books
Body - 
{"book":"GodFather","price":350.00,"description":"About the Dons of Italy","rating": 5,"isbn":"10234485","pub_date":"1969-05-01 00:00:00","author":"Mario Puzzo"} 
Response - status 201 CREATED

Request Method : GET Method -  http://127.0.0.1:5000/api/books (Can be used to get all the book details or search a specific book/author)
Response - status 200 OK

Request Method : PUT Method -  http://127.0.0.1:5000/api/book/<ObjectId>
Body - 
{"book":"GodFather2","price":350.00,"description":"About the Dons of Italy","rating": 4,"pub_date":"1989-05-01 00:00:00","author":"Mario Puzzo"
} 
Response - status 200 OK

Request Method : PATCH Method -  http://127.0.0.1:5000/api/book/<ObjectId>
Body - 
{"price":400.00
} 
Response - status 200 OK

Request Method : DELETE Method -  http://127.0.0.1:5000/api/book/<ObjectId>
Response - status 204 NO CONTENT

Request Method : GET Method -  http://127.0.0.1:5000/api/book/<ObjectId> (To select a book based on the object id)
Response - status 200 OK

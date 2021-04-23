from flask_restplus import Resource
# from flask import Blueprint, Response, request
# from database.models import Movie
from flask import Response, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flaskbook.db import db
from werkzeug.utils import cached_property
class BooksApi(Resource):
    def get(self):
        a = request.args.get('author', None)
        b = request.args.get('book', None)

        print("aa:", a)
        if a or b:
            book = db.db.book.find({'$or':[{'author': a},{'book':b}]})

        else:
            print("bb")
            book = db.db.book.find()
            # print("id:",book['$oid'])
            # resp = dumps(book)
            # return resp
        output = []
        resp = dumps(book)
        for s in book:
            output.append({'name': s['book'], 'author': s['author'], 'price': s['price']
                              , 'rating': s['rating'], 'isbn': s['isbn'], 'pubdate': s['pubdate']})

        return jsonify({"result:": resp})

    def post(self):
        _json = request.json
        _book = _json['book']
        _author = _json['author']
        _price = _json['price']
        _rating = _json['rating']
        _isbn = _json['isbn']
        _pubdate = _json['pubdate']

        if _book and _author and _price and _rating and _isbn and _pubdate and request.method == 'POST':
            # _hashed_password = generate_password_hash(_password)
            id = db.db.book.insert(
                {'book': _book, 'author': _author, 'price': _price, 'rating': _rating
                    , 'isbn': _isbn, 'pubdate': _pubdate})
            resp = jsonify("Book added successfully!!")
            resp.status_code = 201
            return resp


class BookApi(Resource):
    def put(self, id):
        _json = request.json
        _id = id
        _book = _json['book']
        _author = _json['author']
        _price = _json['price']
        _rating = _json['rating']
        _isbn = _json['isbn']
        _pubdate = _json['pubdate']

        if _book and _author and _price and _rating and _isbn and _pubdate and request.method == 'PUT':
            # _hashed_password = generate_password_hash(_password)
            db.db.book.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':
                {
                    'book': _book,
                    'author': _author,
                    'price': _price,
                    'rating': _rating,
                    'isbn': _isbn,
                    'pubdate': _pubdate}})
            resp = jsonify("Book updated successfully!!")
            resp.status_code = 200
            return resp


    def delete(self, id):
        user = db.db.book.delete_one({'_id': ObjectId(id)})
        resp = jsonify("User deleted successfully")
        resp.status_code = 204
        return resp

    def get(self, id):
        user = db.db.book.find_one({'_id': ObjectId(id)})
        resp = dumps(user)
        return resp

    def patch(self, id):
        _json = request.json
        _id = id
        # _name = _json['name']
        # _casts = _json['casts']
        # _genres = _json['genres']

        if _json and request.method == 'PATCH':
            # _hashed_password = generate_password_hash(_password)
            db.db.book.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':
                                                                                                            _json})
            resp = jsonify("Movie patched successfully!!")
            resp.status_code = 200
            return resp

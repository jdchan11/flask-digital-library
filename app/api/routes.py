from urllib import response
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Books, book_schema, books_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/books', methods = ['POST'])
@token_required
def create_book(current_user_token):
    isbn_number = request.json['isbn_number']
    book_title = request.json['book_title']
    book_length = request.json['book_length']
    author = request.json['author']
    cover_type = request.json['cover_type']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    book = Books(isbn_number, book_title, book_length, author, cover_type, user_token = user_token)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods = ['GET'])
@token_required
def get_books(current_user_token):
    a_user = current_user_token.token
    books = Books.query.filter_by(user_token = a_user).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_book(current_user_token, id):
    book = Books.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('books/<id>', methods = ['POST', 'PUT'])
@token_required
def update_book(current_user_token, id):
    book = Books.query.get(id)
    book.isbn_number = request.json['isbn_number']
    book.book_title = request.json['book_title']
    book.book_length = request.json['book_length']
    book.author = request.json['author']
    book.cover_type = request.json['cover_type']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)
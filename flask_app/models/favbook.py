from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
from flask_app.models.author import Author
class Favbook:
    def __init__( self , data ):
        self.id = data['id']
        self.book_id = data['book_id']
        self.author_id = data['author_id']
    @classmethod
    def get_all( cls,data):
        query="SELECT title,page_number,book_id FROM favbooks JOIN books ON books.id=favbooks.book_id LEFT JOIN authors ON authors.id=favbooks.author_id WHERE favbooks.author_id=%(id)s;"
        return connectToMySQL('booksandusers').query_db( query,data)
    @classmethod
    def save( cls,data):
        query='INSERT INTO favbooks (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);'
        return connectToMySQL('booksandusers').query_db( query,data)
    @classmethod
    def delete( cls,data):
        query='DELETE FROM favbooks WHERE book_id=%(id)s;'
        return connectToMySQL('booksandusers').query_db( query,data)
    @classmethod
    def get_all_authors( cls,data):
        query="SELECT name FROM favbooks LEFT JOIN books ON books.id=favbooks.book_id LEFT JOIN authors ON authors.id=favbooks.author_id WHERE favbooks.book_id=%(id)s;"
        return connectToMySQL('booksandusers').query_db( query,data)

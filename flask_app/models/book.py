from flask_app.config.mysqlconnection import connectToMySQL
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.page_number = data['page_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('booksandusers').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    @classmethod
    def save(cls, data):
        query="INSERT INTO books (title,page_number,created_at,updated_at) VALUES(%(title)s,%(page_number)s,now(),now())"
        return connectToMySQL('booksandusers').query_db(query,data)
    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM books WHERE id=%(id)s"
        return connectToMySQL('booksandusers').query_db(query,data)[0]
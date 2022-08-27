from flask_app.config.mysqlconnection import connectToMySQL
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('booksandusers').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, now(), now())"
        return connectToMySQL('booksandusers').query_db(query,data)
    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM authors WHERE id=%(id)s"
        return connectToMySQL('booksandusers').query_db(query,data)[0]
    @classmethod
    def delete(cls, data):
        query="DELETE FROM favbooks WHERE author_id=%(id)s"
        connectToMySQL('booksandusers').query_db(query,data)
        query="DELETE FROM authors WHERE id=%(id)s"
        return connectToMySQL('booksandusers').query_db(query,data)

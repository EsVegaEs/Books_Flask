from flask import  render_template,request,redirect,session,url_for
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favbook import Favbook
from flask_app import app

@app.route("/")
def index():
    return redirect('/authors')

@app.route("/authors")
def authors():
    return render_template('authors.html',authors=Author.get_all())

@app.route('/addauthor',methods=['post'])
def addauthor():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/showauthor/<int:id>')
def showauthor(id):
    data={
        'id':id,
    }
    return render_template('authorshow.html',author=Author.get_one(data),fbooks=Favbook.get_all(data),books=Book.get_all())

@app.route('/addauthorfav/<int:id>',methods=['post'])
def addauthorfav(id):
    data={
        'id':id,
    }
    data1={
        'book_id':request.form['title'],
        'author_id':request.form['author_id']
    }
    Favbook.save(data1)
    print(Favbook.get_all(data1))
    return render_template('authorshow.html',author=Author.get_one(data),fbooks=Favbook.get_all(data),books=Book.get_all())

@app.route('/deleteauthor/<int:id>')
def deleteauthor(id):
    data={
        'id':id,
    }
    Author.delete(data)
    return redirect('/authors')


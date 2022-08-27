from flask import  render_template,request,redirect,session,url_for
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favbook import Favbook
from flask_app import app

@app.route('/deletebook/<int:id>')
def deletebook(id):
    data={ 'id': id }
    Favbook.delete(data)
    data={ 'id': id }
    return redirect('/')

@app.route('/addnewbook',methods=['POST'])
def addnewbook():
    Book.save(request.form)
    return redirect('/addbook')

@app.route('/addbook')
def addbook():
    return render_template('bookshow.html',books=Book.get_all())

@app.route('/book/<int:id>')
def bookshow(id):
    data={ 'id': id }
    return render_template('books.html',book=Book.get_one(data),authors=Favbook.get_all_authors(data),allauthors=Author.get_all())

@app.route('/addbookfav/<int:id>',methods=['POST'])
def addbookfav(id):
    data={
        'id':id,
    }
    data1={
        'book_id':request.form['book_id'],
        'author_id':request.form['name']
    }
    Favbook.save(data1)
    return redirect(url_for('.bookshow',book=Book.get_one(data),authors=Favbook.get_all_authors(data),allauthors=Author.get_all(),id=data['id']))

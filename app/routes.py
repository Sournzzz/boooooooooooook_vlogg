from app import app 
from flask import render_template, url_for, flash  
from app.forms import BookSearchForm, BookAddForm

@app.route("/")
@app.route("/home")
def index(): 
    return render_template("home.html", title="Home")

@app.route("/books/search", methods=["GET", "POST"])
def booksearch():
    form = BookSearchForm() 
    titlebook = form.titlebook.data
    author = form.author.data
    if form.validate_on_submit(): 
        return redirect()
    return render_template('search_book.html', titlebook= titlebook, title="Search", author=author, form=form)


@app.route("/books/add", methods=["GET", "POST"])
def bookadd(): 
    form = BookAddForm()
    titlebook = form.titlebook.data
    author = form.author.data 
    if form.validate_on_submit():
        flash (f'Book {titlebook} submitted succesfully. Author: {author}')
    return render_template('search_book.html', titlebook= titlebook, title="Search", author=author, form=form)

@app.route("/books")
def show_books():
    books 
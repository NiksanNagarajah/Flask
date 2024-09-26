from .app import app
from flask import render_template
from .models import get_sample

@app.route('/')
# def home():
#     return "<h1>Hello World !</h1>"
def home():
    return render_template(
        'home.html', 
        title="My Books !",
        books=get_sample())

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = get_sample()[int(id)]
    print(book)
    return render_template(
        'detail.html',
        book=book,
    )
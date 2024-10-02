from .app import app
from flask import render_template
from .models import *

@app.route('/')
def home():
    return render_template(
        'home.html', 
        title="My Books !",
        books=get_sample())

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = get_sample()[int(id)-1]
    print(book)
    return render_template(
        'detail.html',
        book=book,
    )

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from flask import render_template

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template(
        "edit-author.html",
        author=a,
        form=f
    )

from flask import url_for, redirect, render_template
from .app import db
from .models import Author

@app.route("/save/author/", methods=("POST",))
def save_author():
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('edit_author', id=a.id))
    # Si la validation échoue, on récupère à nouveau l'auteur
    a = get_author(int(f.id.data))
    return render_template(
        "edit-author.html",  # Correction du nom du template
        author=a,
        form=f
    )

@app.route("/save/newAuthor", methods=("POST",))
def save_new_author():
    f = AuthorForm()
    if f.validate_on_submit():
        a = Author(name=f.name.data)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('authors'))
    return render_template(
    "new-author.html",
    form=f)

@app.route("/authors")
def authors():
    return render_template(
        "authors.html",
        authors=get_authors()
        )

@app.route("/author/newAuthor")
def newAuthor():
    id = Author.query.count() + 1
    form = AuthorForm(id=id)
    if form.validate_on_submit():
        if form.name.data == "":
            flash('Le nom de l\'auteur est obligatoire !')
            return redirect(url_for('newAuthor'))
        new_author = Author(name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
        flash('Auteur enregistré avec succès !')
        return redirect(url_for('authors'))
    return render_template(
        "new-author.html",
        form=form
        )

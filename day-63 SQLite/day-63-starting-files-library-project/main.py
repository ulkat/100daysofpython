from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()



@app.route('/')
def home():

    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = request.form['book']
        author = request.form['author']
        rating = request.form['rating']
        new_dic = {
            "title": book,
            "author": author,
            "rating": rating
        }
        with app.app_context():
            new_book = Book(title=new_dic["title"], author=new_dic["author"], rating=new_dic["rating"])
            db.session.add(new_book)
            db.session.commit()


        return redirect(url_for('home'))
    else:
        return render_template('add.html')



if __name__ == "__main__":
    app.run(debug=True)


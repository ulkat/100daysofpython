    from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.

'''

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db.init_app(app)
Bootstrap5(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()
class EditForm(FlaskForm):
    rating = FloatField('Your ratinf out of /10 ? ', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    movie_title = StringField('Movie Title ', validators=[DataRequired()])
    submit = SubmitField('Add')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.id))
    all_movies = result.scalars().all() # convert ScalarResult to python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", all_movies=all_movies)

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_to_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if edit_form.validate_on_submit():
        movie_to_edit.rating = edit_form.rating.data
        movie_to_edit.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, movie=movie_to_edit)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add")
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


if __name__ == '__main__':
    app.run(debug=True)

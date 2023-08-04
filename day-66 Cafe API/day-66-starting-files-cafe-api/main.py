import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
API_KEY = "TopSecretAPIKey"

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()
    random_cafe = random.choice(all_cafe)
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()
    cafe_list = [item.to_dict() for item in all_cafe]
    return jsonify(cafes=cafe_list)

@app.route("/search")
def get_search():
    query_location = request.args.get("loc")
    result = db.session.query(Cafe).filter(Cafe.location == query_location)
    all_cafe_with_loc = result.all()
    cafe_list = [item.to_dict() for item in all_cafe_with_loc]
    if cafe_list:
        return jsonify(cafes=cafe_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully changed the price."})
    else:
        return jsonify(response={"error": "no id like that."})

## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        if api_key == API_KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(response={"error": "Sorry thats not allowed. 403"})
    else:
        return jsonify(response={"error": "no id like that."})

if __name__ == '__main__':
    app.run(debug=True)

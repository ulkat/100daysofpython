from flask import Flask, render_template
from datetime import datetime
import requests

MY_NAME = "FAHRİ ULKAT"


app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year

    return render_template("index.html", current_year=current_year, my_name=MY_NAME)

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_date = age_response.json()

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()

    return render_template("guess_page.html", name=name.title(), gender=gender_data["gender"], age=age_date["age"])

if __name__ == "__main__":
    app.run(debug=True)
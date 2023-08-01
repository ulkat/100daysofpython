from flask import Flask
import random

app = Flask(__name__)

random_number = str(random.randint(0, 9))

@app.route("/")
def main_page():
    return '<h1 style = "color: Blue ">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>'

@app.route("/<number>")
def guess(number):
    if number == random_number:
        return '<h1 style = "color: green">You are correct!!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'
    elif number < random_number:
        return '<h1 style = "color:red">You are too low!!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>'
    elif number > random_number:
        return '<h1 style = "color:purple">You are too high!!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>'


if __name__ == "__main__":
    app.run(debug=True)
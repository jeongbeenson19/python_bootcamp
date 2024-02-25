from flask import Flask, render_template
from random import randint

app = Flask(__name__)

number = randint(0, 9)


def higher_lower(function):
    def wrapper(_int):
        if _int > number:
            img = ("<h1>Too high</h1>"
                   "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif alt=too high>")
            return function(_int, img)
        elif _int < number:
            img = ("<h1>Too low</h1>"
                   "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif alt=too low>")
            return function(_int, img)
        else:
            img = ("<h1>You found me</h1>"
                   "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif alt=correct>")
            return function(_int, img)
    return wrapper


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/<int:_int>')
@higher_lower
def answer_page(_int, img):
    return "<h1>{}</h1>{}".format(_int, img)


if __name__ == "__main__":
    app.run(debug=True)

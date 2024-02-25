from flask import Flask
import main.html

app = Flask(__name__)


@app.route('/')
def hello_world():
    return main.html


if __name__ == "__main__":
    app.run(debug=True)

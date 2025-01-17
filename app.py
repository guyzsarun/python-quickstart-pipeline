from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/square/<int:number>")
def calculate(number):
    if number <= 0:
        return "Number cannot be less than 0"
    return "{} squared is {}".format(number, number**2)


if __name__ == "__main__":
    app.run(debug=True)

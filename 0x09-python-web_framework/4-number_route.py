#!/usr/bin/python3

"""Script starts Flask web Application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def C(text):
    return ("C " + text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    return ("Python " + text.replace("_", " "))


@app.route('/number/<int:n>')
def is_number(n):
    return ("{} is a number".format(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

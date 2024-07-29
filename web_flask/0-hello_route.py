#!/usr/bin/python3
from flask import Flask
""" The script that start a Flask web application """

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ First route flask application """
    return f"Hello HBNB!"

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 5000
    app.run(host=HOST, port=PORT)

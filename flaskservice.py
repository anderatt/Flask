#!/usr/bin/python3

from flask import Flask # type: ignorecccc
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(host="0.0.0.0")

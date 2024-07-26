#!/usr/bin/python3

from flask import Flask # type: ignore
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db')
def db_access():
    return 'Acessando o Database!'

@app.route('/app')
def db_access():
    return 'Acessando o APP!'

@app.route('/box')
def box_access():
    return 'Acessando o BOX!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

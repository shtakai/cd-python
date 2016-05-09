from flask import Flask, request, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = "oerjtoidgeq3jg"


@app.route('/users', methods=['GET'])
def index():
    pass


@app.route('/users/new', methods=['GET'])
def new():
    pass


@app.route('/users/<id>/edit'. methods=['GET'])
def edit(id):
    pass


@app.route('/usrs/<id>', methods=['GET'])
def show(id):
    pass


@app.route('/users/create', methods=['POST'])
def create():
    pass


@app.route('/users/<id>/destroy', methods=['GET'])
def destroy(id):
    pass


@app.route('/uers/<id>', methods=['POST'])
def update(id):
    pass



app.run(debug=True)


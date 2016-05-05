from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/friends', methods=['POST'])
def create():
    return redirect('/')


app.run(debug=True)


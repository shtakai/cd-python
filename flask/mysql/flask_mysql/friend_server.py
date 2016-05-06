from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/friends/<friend_id>', methods=['POST'])
def create(friend_id):
    query = "select * from friends where id= :specific_id"
    specific_id = {'specific_id': friend_id}
    friends = mysql.query_db("select * from friends where id= :specific_id")
    # print friends
    return render_template('index.html', all_friends=friends)


app.run(debug=True)


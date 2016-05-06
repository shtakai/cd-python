from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/friends/<friend_id>')
def index_friend(friend_id):
    query = "select * from friends where id= :specific_id"
    data= {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    print friends
    return render_template('index.html', all_friends=friends[0])


@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    return redirect('/')


app.run(debug=True)


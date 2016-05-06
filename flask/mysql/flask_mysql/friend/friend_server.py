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
    query = "insert into friends (first_name, last_name, occupation, created_at, updated_at) values (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "update friends set first_name = :first_name, last_name = :last_name, occupation = :occupation where id = :id"
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'occupation': request.form['occupation'],
            'id': friend_id
            }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/remove_friend/<friend_id>', methods=['POST'])
def remove(friend_id):
    query = "delete from friends where id = :id"
    data = { 'id': friend_id }
    mysql.query_db(query,data)
    return redirect('/')


app.run(debug=True)


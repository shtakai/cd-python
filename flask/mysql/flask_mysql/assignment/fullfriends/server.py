from flask import Flask, request, redirect, render_template,  flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = "oerjtoiq3jg"

@app.route('/')
def index():
    '''
        Display all of the friends on the index.html page
    '''
    query = "select * from friends"
    friends = mysql.query_db(query, {})
    return render_template('index.html', friends=friends)


@app.route('/friends', methods=['POST'])
def create():
    '''
        Handle the add friend form submit and create the friend in the DB
    '''
    query = "insert into friends (first_name, last_name, occupation, created_at, updated_at) values (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    flash("Added New User: {} {}".format(data['first_name'], data['last_name']))
    return redirect('/')


@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    '''
        Display the edit friend page for the particular friend
    '''
    friend = ""
    suffix = ""
    if id=="_":
        friend = {
            'id': '',
            'first_name': '',
            'last_name': '',
            'occupation': ''
        }
        title = "Add"
    else:
        query = "select * from friends where id= :specific_id"
        data= {'specific_id': id}
        friends = mysql.query_db(query, data)
        friend=friends[0]
        title = "Edit"
        suffix = "/{}".format(friend['id'])

    return render_template('edit.html', friend=friend, title=title, suffix=suffix)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    '''
        Handle the edit friend form submit and update the friend in the DB
    '''
    query = "update friends set first_name = :first_name, last_name = :last_name, occupation = :occupation where id = :id"
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'occupation': request.form['occupation'],
            'id': id
            }
    mysql.query_db(query, data)
    flash("Updated {} {}".format(data['first_name'], data['last_name']))
    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    '''
        Delete the friend from the DB
    '''
    query = "select * from friends where id = :id"
    data = { 'id': id }
    friend = mysql.query_db(query, data)[0]
    query = "delete from friends where id = :id"
    mysql.query_db(query,data)
    flash("Deleted friend {} {}".format(friend['first_name'], friend['last_name']))
    return redirect('/')


app.run(debug=True)


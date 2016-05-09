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
    users_query = "select id,first_name, last_name, email,created_at from users"
    users = mysql.query_db(users_query, {})
    return render_template('index.html', users=users)


@app.route('/users/new', methods=['GET'])
def new():
    return render_template('new.html')


@app.route('/users/<id>/edit', methods=['GET'])
def edit(id):
    user_query = "select id, first_name, last_name, email, created_at from users where id = :id limit 1"
    user_data = { 'id': id }
    user = mysql.query_db(user_query, user_data)[0]
    return render_template('edit.html',user=user)


@app.route('/users/<id>', methods=['GET'])
def show(id):
    user_query = "select id, first_name, last_name, email, created_at from users where id = :id limit 1"
    user_data = { 'id': id }
    user = mysql.query_db(user_query, user_data)[0]
    return render_template('show.html',user=user)


@app.route('/users/create', methods=['POST'])
def create():
    if not request.form['first_name'] or not request.form['last_name'] or not request.form['email']:
        flash("All forms should be filled")
        return redirect('/users/new')

    user_query = "insert into users ( first_name, last_name, email, created_at, updated_at ) values (:first_name, :last_name, :email, NOW(), NOW())"
    user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(user_query, user_data)
    flash("user {} {} created.".format(request.form['first_name'], request.form['last_name']))
    return redirect('/users')


@app.route('/users/<id>/destroy', methods=['GET'])
def destroy(id):
    user_query = "delete from users where id = :id"
    user_data = { 'id': id }
    mysql.query_db(user_query, user_data)
    flash ("User id:{} is deleted".format(id))
    return redirect('/users')


@app.route('/users/<id>', methods=['POST'])
def update(id):
    user_query = "update users set first_name = :first_name, last_name = :last_name, email = :email, updated_at=NOW() where id = :id"
    user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
            }
    mysql.query_db(user_query, user_data)
    flash("Updated User: {}".format(id))
    return redirect('/users')


# helper method
def get_method():
    sys._getframe().f_code.co_name


app.run(debug=True)


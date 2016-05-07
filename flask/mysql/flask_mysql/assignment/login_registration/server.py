from flask import Flask, request, render_template, redirect, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = "oerjtoidgeq3jg"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register_top', methods=['GET'])
def register_top():
    return render_template('register.html')



@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    pw_hash = bcrypt.generate_password_hash(password)

    insert_query = "insert into users (email, username, pw_hash, created_at) values (:email, :username, :pw_hash, NOW())"
    query_data = { 'email': email, 'username': username, 'pw_hash': pw_hash}
    mysql.query_db(insert_query, query_data)
    flash("Created user")
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "select * from users where email = :email limit 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        print 'login user'
    else:
        print 'login error'

    return render_template('index.html')


app.run(debug=True)


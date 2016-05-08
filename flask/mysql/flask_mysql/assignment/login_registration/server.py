from flask import Flask, request, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
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


@app.route('/login_top', methods=['GET'])
def login_top():
    return render_template('login.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    session['error'] = ""

    print email

    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    password_pattern = r"^[a-zA-Z0-9]{8}?"
    if(not re.match(email_pattern, request.form['email'])):
        messages = "Email is not valid!"
        session['error'] += messages
        flash(messages)
        print "email not valid"

    if(not re.match(password_pattern, request.form['password'])):
        messages = "Password must be at least 8 letters"
        session['error'] += messages
        flash(messages)
        print "password is not invalid"

    if(request.form['password'] != request.form['confirm_password']):
        messages = "Password and Password confirmation don't match"
        session['error'] += messages
        flash(messages)
        print messages

    if session['error']:
        print "register error"
        return render_template('register.html', username=username, email=email)

    else:
        print "email is okay"
        pw_hash = bcrypt.generate_password_hash(password)
        insert_query = "insert into users (email, username, pw_hash, created_at) values (:email, :username, :pw_hash, NOW())"
        query_data = { 'email': email, 'username': username, 'pw_hash': pw_hash}
        mysql.query_db(insert_query, query_data)
        flash("Created user")
        username = ""
        password = ""
        email = ""

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "select * from users where email = :email limit 1"
    query_data = { 'email': email }
    users = mysql.query_db(user_query, query_data)
    print users
    print 'not users', not users
    if( users and bcrypt.check_password_hash(users[0]['pw_hash'], password)):
        flash('login user')
        session['user'] = users[0]['id']
    else:
        flash('email or password is wrong. please check')

    return render_template('index.html')


app.run(debug=True)


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
    # find messages -> user,comment ->user
    posts = {}
    posts_query = "select messages.message, messages.id, messages.user_id, messages.created_at, users.username from messages inner join users on messages.user_id = users.id order by messages.created_at desc"
    posts = mysql.query_db(posts_query,{});
    # print posts
    comments_hash = {}
    for post in posts:
        comments_query = "select * from comments where message_id = :message_id order by created_at desc"
        comments_data = {'message_id': post['id']}
        comments = mysql.query_db(comments_query, comments_data)
        # print 'comments', comments
        comments_hash[post['id']] = comments

    print comments_hash
    return render_template('index.html', posts=posts, comments=comments_hash)


@app.route('/create_post', methods=['POST'])
def create_post():
    # precondition: already logged in
    print "create_post", session['user'], session['username']
    if not session['user']:
        message="You should log in"
        flash(message)
        print message
    else:
        # get post from form and redirect
        # check validation presence of message
        print "insert query"
        post_query = "insert into messages (message, user_id, created_at, updated_at) values (:message, :user_id, NOW(), NOW())"
        if not request.form['message']:
            message = "Message is empty!"
            flash(message)
            print message
        else:
            print post_query
            post_data = {
                    'message': request.form['message'],
                    'user_id': session['user']
                    }
            print "*" * 50
            print "data", post_data
            mysql.query_db(post_query, post_data)
            print "insert_query finished"
    return redirect('/')


@app.route('/messages/<message_id>/create_comment', methods=['POST'])
def create_comment(message_id):
    # precondition check the message id (present!)
    message_query = "select * from messages where id = :message_id limit 1"
    message_data = { 'message_id': message_id }
    print message_id,message_query
    print request.form
    messages = mysql.query_db(message_query, message_data)
    message = messages[0]
    print message['message']
    comment = request.form['comment']
    if not session['user']:
        m = "not log in"
        flash(m)
        print m
    elif not message:
        m = "invalid message id"
        flash(m)
        print m
    elif not request.form['comment']:
        m = "comment is empty"
        flash(m)
        print m
    else:
        # insert comment
        comment_query = "insert into comments (comment, user_id, message_id, created_at, updated_at) values (:comment, :user_id, :message_id, NOW(), NOW())"
        print "*" * 50
        print message_id
        comment_data = {
                'comment': request.form['comment'],
                'user_id': session['user'],
                'message_id': message_id
                }
        mysql.query_db(comment_query, comment_data)
        print "comment inserted", comment_data

    return redirect('/')



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

    return redirect('/')


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
        session['username'] = users[0]['username']
    else:
        flash('email or password is wrong. please check')

    return redirect('/')


app.run(debug=True)


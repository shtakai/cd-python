from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key="43tu4jgoerk"
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emails',methods=['POST'])
def create_email():
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if(not re.match(email_pattern, request.form['email'])):
        message = "Email is not valid!"
        session['error'] = message
        print message
        return redirect('/')
    else:
        query = "insert into emails (email, created_at, updated_at) values (:email, NOW(), NOW())"
        email = request.form['email']
        data = {
            'email': email
        }
        print request.form['email']
        mysql.query_db(query, data)
        session.clear()
        query = "select * from emails"
        data= {}
        emails = mysql.query_db(query, data)
        print emails
        return render_template('success.html', email=email, emails=emails)

app.run(debug=True)


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


@app.route('/delete_email/<id>', methods=["POST"])
def remove_email(id):
    deleted = ""
    query = "select id from emails where id = :id"
    data = {'id': id}
    ids = mysql.query_db(query, data)
    if(not ids):
        flash("invalid id for deleting")
    else:
        query = "delete from emails where id = :id"
        mysql.query_db(query, data)
        deleted = "deleted id: {}".format(id)

    query = "select * from emails"
    emails = mysql.query_db(query, {})
    print emails
    return render_template('success.html', emails = emails, deleted=deleted)


app.run(debug=True)


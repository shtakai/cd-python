from flask import Flask, render_template, redirect, request, session, flash
import re
app = Flask(__name__)
app.secret_key = "rkgjrmy5945ym4w"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja/<ninja_color>')
def ninja(ninja_color):
    print ninja_color
    ninja_obj = {
                'blue': 'leonardo',
                'orange': 'michelangelo',
                'red': 'raphael',
                'purple': 'donatello'
            }
    if ninja_obj.get(str(ninja_color)):
        ninja = ninja_obj[str(ninja_color)]
    else:
        ninja = False

    print ninja_color, ninja


    return render_template('ninja.html', ninja=ninja)

'''
@app.route('/')
def index():
    # remove completed in session
    if session.get('completed'):
        session.clear()
        session['completed'] = 'completed'


    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    messages = []
    for form_element in request.form:
        # check empty form_element
        #print request.form[form_element]
        if form_element == "submit":
            continue
        if len(request.form[form_element]) < 1:
            #print "empty error"
            messages.append("{} cannot be empty.".format(form_element.capitalize()))
    for message in sorted(messages):
        flash(message)

    # check the length of email
    if len(request.form['email']) < 8 :
        flash("email should be more than 8 characters")
        messages.append("email")

    # check numbers in first_name and last_name
    number_pattern = r".*\d+.*"
    # print re.match(number_pattern, request.form['first_name'])
    # print re.match(number_pattern, request.form['last_name'])
    if( re.match(number_pattern, request.form['first_name']) or
        re.match(number_pattern, request.form['last_name'] )):
        flash("First and Last Name cannot contain any numbers")
        messages.append("name")

    # check valid email address
    # TODO: revise the pattern  it isn't complete.
    email_pattern = "[^@]+@([^@]+\.)*\w+\.\w+"
    #print re.match(email_pattern, request.form['email'])

    if(not re.match(email_pattern, request.form['email'])):
        flash("Email should be a valid email")
        messages.append("email")

    # check that password equals confirm_password
    if(request.form['password'] != request.form['confirm_password']):
        flash("Password and Password Confirmation should match")
        messages.append("password")

    # set elements to sessions
    for form_element in request.form:
        if form_element == 'password' or form_element == 'confirm_password':
            request.form[form_element] == ""
        session[form_element] = request.form[form_element]

    # if form is completely good, set completed=True
    if len(messages) == 0:
        session['completed'] = "completed"
        #print 'completed'

    return redirect('/')
'''

app.run(debug=True, port = 8000)

from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "XXXXXXXXXX"


def add_count(num):
    if(session.get('count') > 0):
        session['count'] += num
    else:
        session['count'] = num


@app.route('/')
def index():
    return redirect('show_counter')


@app.route('/add2')
def add2():
    add_count(2)
    return render_template('index.html', count=session['count'])


@app.route('/reset')
def reset():
    session['count'] = 0
    return render_template('index.html', count=session['count'])


@app.route('/show_counter')
def show_counter():
    add_count(1)
    return render_template('index.html', count=session['count'])


app.run(debug=True)

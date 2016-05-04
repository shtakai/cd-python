from flask import Flask, render_template, request, session, redirect, flash
import random
app = Flask(__name__)
app.secret_key = "XXXXXXXX"


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(0, 101)
    print session['number']
    if request.method == 'POST':
        print request.form['guess']
        number = 0
        try:
            guess = int(request.form['guess'])
            if session['number'] == guess:
                number = session.pop('number')
                guess_result = "WINNING"
            elif session['number'] > guess:
                guess_result = "LOW"
            else:
                guess_result = "HIGH"
        except Exception:
            guess_result = "NOT"
        return render_template(
            'index.html',
            guess_result=guess_result,
            number=number
        )
    else:
        return render_template('index.html')


app.run(debug=True)

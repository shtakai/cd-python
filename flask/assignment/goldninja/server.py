from flask import Flask, render_template, request, session, redirect, flash
import random
from datetime import datetime as dt
app = Flask(__name__)
app.secret_key = "hgrefjndsj43u32"


@app.route('/', methods=['GET'])
def index():
    if 'gold' not in session:
        print 'create gold in session'
        session['gold'] = 0
    if 'messages' not in session or session['messages'] == None:
        print 'create messages in session'
        session['messages'] = []
    gold = int(session['gold'])
    messages = session['messages']
    print 'gold:', session['gold'],'messages:', session['messages']

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    print 'process_money', request.form
    house_type = request.form['house_type']
    message_template = "Earn a {} and {} golds... {} ({})"
    say = ""
    say_class = ""
    tdatetime = dt.now()
    datetime = tdatetime.strftime('%Y/%m/%d %I:%M%p')
    # datetime = "11/11/11"
    print 'house_type', house_type
    if house_type == 'farm':
        earn_gold = random.randint(10, 21)
    elif house_type == 'cave':
        earn_gold = random.randint(5, 11)
    elif house_type == 'house':
        earn_gold = random.randint(2, 6)
    elif house_type == 'casino':
        casino_win = random.randint(-1,1)
        if(casino_win > 0):
            earn_gold = random.randint(0, 51)
        else:
            earn_gold = -1 * random.randint(0, 51)
            say = "Ouch"
            say_class = "class=ouch"
    else:
        ''' do nothing '''
        pass
    print 'earn_gold:', earn_gold, 'house_type:', house_type, 'say:', say, 'datetime:', datetime, 'say_class:', say_class
    message = message_template.format(earn_gold, house_type, say, datetime )
    session['gold'] = int(session['gold']) + earn_gold

    session['messages'].append({'message':message, 'class': say_class})
    print 'gold:', session['gold'],'messages:', session['messages']

    return redirect('/')


'''
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
'''

app.run(debug=True)

"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Processmoney(Controller):
    def __init__(self, action):
        super(Processmoney, self).__init__(action)

    def index(self):
        if not session.get('gold'):
            session['gold'] = 0
        if not session.get('activities'):
            session['activities'] = []
        return self.load_view('index.html')

    def process_money(self):
        if not request.form.get('house_type'):
            # error handling
            pass
        house_type = request.form['house_type']
        if house_type == 'farm':
            earn = random.randint(2, 5)
        elif house_type == 'cave':
            earn = random.randint(5, 10)
        elif house_type == 'house':
            earn = random.randint(2, 5)
        elif house_type == 'casino':
            earn = random.randint(-50, 50)
        else:
            # error handling
            pass

        if earn >= 0:
            activity = "Earned {} gold(s) from the {}! {}".format(earn, house_type, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p'))
            css = "green"
        else:
            activity = "Entered a {} and lost {} gold(s)... ouch {}".format(house_type, abs(earn), datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p'))
            css = "red"

        session['activities'].insert(0,{
            'activity': activity,
            'class': css
            })
        session['gold'] += earn

        return redirect('/')

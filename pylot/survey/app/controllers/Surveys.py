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

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def process(self):
        # Validate the form
        if not request.form['name'] or not request.form['location'] and not request.form['language']:
            flash("Name, Location and Language is mandatory")
            return redirect('')

        # Then store sesison
        session['name']     = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment']  = request.form['comment']
        return redirect('/result')

    def result(self):
        if not session.get( 'name' ) or not session.get( 'location' ) or not session.get( 'language' ):
            return redirect('/')

        if not session.get( 'count' ):
            session['count'] = 1
        else:
            session['count'] += 1

        name     = session['name']
        location = session['location']
        language = session['language']
        comment  = session['comment']

        del(session['name'])
        del(session['location'])
        del(session['language'])
        del(session['comment'])

        return self.load_view('result.html', name=name, location=location, language=language, comment=comment)

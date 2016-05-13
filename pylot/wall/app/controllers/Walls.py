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

class Walls(Controller):
    def __init__(self, action):
        super(Walls, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('Wall')

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        # print self.models['Wall'].get_all_users()
        if not session.get('user'):
            return self.load_view('login.html')

        return self.load_view('index.html')

    def login(self):
        print request.form
        user = self.models['Wall'].login(request.form)
        if user:
            session['user'] = user[1]
            return redirect('/')
        else:
            flash("login failed")
            return self.load_view('login.html')

    def register(self):
        print request.form
        user = self.models['Wall'].register(request.form)
        print user
        if user:
            print 'register succeed'
        else:
            print 'register failed'

        return self.load_view('login.html')

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

class Randomword(Controller):
    def __init__(self, action):
        super(Randomword, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('index.html')

    def get_random_string(self):
        """
         get random word
        """
        if not session.get('attempts'):
            session['attempts'] = 1
        else:
            session['attempts'] += 1

        random_word = ''
        for i in range(0,14):
            random_word += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                )
        session['random_word'] = random_word
        return redirect('/')


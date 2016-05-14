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
        if not session.get('user'):
            return self.load_view('login.html')
        messages = self.models['Wall'].get_messages().get('messages')
        return self.load_view('index.html', messages=messages)

    def login(self):
        result = self.models['Wall'].login(request.form)
        if result['status']:
            session['user'] = result['user']
            session['user_id'] = result['user_id']
            return redirect('/')
        else:
            flash("login failed")
            return self.load_view('login.html')

    def logout(self):
        session.clear()
        return redirect('/')

    def register(self):
        result = self.models['Wall'].register(request.form)
        for message in result['message']:
            flash(message)
        return self.load_view('login.html')

    def post_message(self):
        result = self.models['Wall'].post_message(request.form,user_id=session['user_id'])
        flash('posted message')
        return redirect('/')

    def post_comment(self):
        result = self.models['Wall'].post_comment(request.form,user_id=session['user_id'])
        flash('posted comment')
        return redirect('/')

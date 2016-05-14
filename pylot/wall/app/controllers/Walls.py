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

        messages = self.models['Wall'].get_messages()
        # print messages

        return self.load_view('index.html', messages=messages)

    def login(self):
        print request.form
        user = self.models['Wall'].login(request.form)
        if user:
            session['user'] = user[1]
            session['user_id'] = user[0]
            print session['user']
            return redirect('/')
        else:
            flash("login failed")
            return self.load_view('login.html')

    def logout(self):
        session.clear()
        return redirect('/')

    def register(self):
        print request.form
        user = self.models['Wall'].register(request.form)
        print user
        if user:
            flash ('register succeed')
        else:
            flash ('register failed')

        return self.load_view('login.html')

    def post_message(self):
        print request.form
        result = self.models['Wall'].post_message(request.form,user_id=session['user_id'])
        flash('posted message')
        return redirect('/')

    def post_comment(self):
        print request.form
        result = self.models['Wall'].post_comment(request.form,user_id=session['user_id'])
        flash('posted comment')
        return redirect('/')

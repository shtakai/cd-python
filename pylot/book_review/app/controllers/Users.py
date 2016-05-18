from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        form = {}
        if session.get('user'):
            return redirect('/books')

        return self.load_view('/index.html', form=form)

    def register(self):
        result = self.models['User'].register(request.form)
        if result.get('errors'):
            self.set_flash(result['errors'], 'error')
            form = dict(request.form)
            del(form['password'])
            del(form['confirm_password'])
            return self.load_view('/index.html', form=form)

        flash('Registration finished. Please Login', 'info')
        return redirect('/')


    def login(self):
        result = self.models['User'].login(request.form)
        if result.get('errors'):
            self.set_flash(result['errors'], 'error')
            return redirect('/')

        flash('logged in', 'info')
        session['user'] = result['user']
        return redirect('/')

    def logout(self):
        session.clear()
        flash('logged out', 'info')
        return redirect('/')

    def show(self, id):
        user_result = self.models['User'].get_user(id)
        if not user_result['status']:
            set_flash(['User not found'], 'error')
            return redirect('/')

        return self.load_view('/users/show.html', user=user_result['user'], books=user_result['reviewed_books'])


from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)
        self.load_model('Review')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def redirect_login(self):
        if session['user']:
            return redirect('/')


    def index(self):
        form = {}
        if session['review']:
            return redirect('/books')

        return self.load_view('/index.html', form=form)

    def destroy(self, id):
        review_result = self.models['Review'].destroy(request.form, id)
        flash('deleted review', 'info')
        return redirect('/')




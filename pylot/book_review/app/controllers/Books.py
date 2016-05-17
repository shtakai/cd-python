from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')
        self.load_model('User')
        self.load_model('Review')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def redirect_login(self):
        if session['user']:
            return redirect('/')


    def index(self):
        self.redirect_login()
        print 'Books#index', request.form
        review_result = self.models['Review'].get_reviews(request.form)
        print "--- review_result", review_result

        book_result = self.models['Book'].get_books_simple(request.form)
        print "--- book_result", book_result

        return self.load_view('/books/index.html', results=review_result['reviews'], books=book_result['books'])

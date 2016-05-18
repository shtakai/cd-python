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
        self.load_model('Author')

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


        return self.load_view('/books/index.html', reviews=review_result['reviews'], books=book_result['books'])

    def new(self):
        self.redirect_login()
        print 'Books#new', request.form
        author_result = self.models['Author'].get_all_authors(request.form)
        print 'author_result', author_result
        return self.load_view('/books/new.html', authors=author_result['authors'])

    def create(self):
        self.redirect_login()
        print 'Books#create', request.form
        book_result = self.models['Book'].create(request.form, session['user']['id'])
        print 'book_result', book_result

        if not book_result['status']:
            set_flash(errors, 'error')
            return redirect('/books/add')

        flash("Added Book and Your Review", 'info')
        return redirect('/books')

    def show(self, id):
        print 'Books#show', request.form, id
        book_result = self.models['Book'].get_book(id)
        print 'book_result', book_result
        if not book_result['status']:
            set_flash(['failed loading book'], 'error')
            return redirect('/')

        return self.load_view('/books/show.html', book=book_result['book_result'], reviews=book_result['review_result'])

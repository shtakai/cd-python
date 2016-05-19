from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')

    def index(self):
        quotes = self.models['Quote'].all()
        return self.load_view('quotes/index.html', quotes=quotes)

    def index_html(self):
        quotes = self.models['Quote'].all()
        return self.load_view('partials/quotes.html', quotes=quotes)

    def index_json(self):
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

    def create(self):
        print 'Quotes#create', request.form
        # the form data is still accessed in the same way as when we normally submitted the form
        # $(this).serialize() helped us send this info over to this url
        new_quote = {
                   "author": request.form['author'],
                   "quote": request.form['quote']
                }
        # we create a quote with our existing model function
        self.models['Quote'].create(new_quote)
        # we then retrieve the updated list of quotes from the database which will include our new quote
        quotes = self.models['Quote'].all()
        # finally we will respond to the AJAX request with a partial that will use the quotes
        # retreived from the database to generate the appropriate html
        return self.load_view('partials/quotes.html', quotes=quotes)

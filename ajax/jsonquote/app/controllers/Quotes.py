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

    # helper methods
    # def set_flash(self, messages, level):
        # for message in messages:
            # flash(message, level)

    def index(self):
        return self.load_view('/quotes/index.html')

    def index_json(self):
        print '---'
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Pokemons(Controller):
    def __init__(self, action):
        super(Pokemons, self).__init__(action)
        self.load_model('Pokemon')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)


    def index(self):
        print 'Pokemons#index', request.form
        return self.load_view('/index.html')


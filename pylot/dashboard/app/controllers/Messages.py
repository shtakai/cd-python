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

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('Message')

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        result = self.models['Message'].get_products()
        if not result['status']:
            flash("failed getting products")

        return self.load_view('index.html', products=result['products'])

    def new(self):
        return self.load_view('new.html')

    def create(self):
        result = self.models['Message'].create_product(request.form)
        if not result['status']:
            for message in result['messages']:
                flash(message)
        else:
            flash('Created Message')
        return redirect('/')

    def show(self, id):
        result = self.models['Message'].get_product(id)
        return self.load_view('show.html', product=result['product'])

    def edit(self, id):

        result = self.models['Message'].get_product(id)
        return self.load_view('edit.html', product=result['product'])

    def update(self, id):
        result = self.models['Message'].update_product(id, request.form)
        if not result['status']:
            for message in result['messages']:
                flash(message)
        else:
            flash('Updated Message')
        return redirect('/')


    def destroy(self):
        result = self.models['Message'].destroy_product(request.form)
        flash('Removed Message Successfully')
        return redirect('/')





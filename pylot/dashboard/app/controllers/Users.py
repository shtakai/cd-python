from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        return self.load_view('index.html')

    # def new(self):
        # return self.load_view('new.html')

    # def create(self):
        # result = self.models['User'].create_User(request.form)
        # if not result['status']:
            # for message in result['messages']:
                # flash(message)
        # else:
            # flash('Created User')
        # return redirect('/')

    # def show(self, id):
        # result = self.models['User'].get_User(id)
        # return self.load_view('show.html', User=result['User'])

    # def edit(self, id):

        # result = self.models['User'].get_User(id)
        # return self.load_view('edit.html', User=result['User'])

    # def update(self, id):
        # result = self.models['User'].update_User(id, request.form)
        # if not result['status']:
            # for message in result['messages']:
                # flash(message)
        # else:
            # flash('Updated User')
        # return redirect('/')


    # def destroy(self):
        # result = self.models['User'].destroy_User(request.form)
        # flash('Removed User Successfully')
        # return redirect('/')





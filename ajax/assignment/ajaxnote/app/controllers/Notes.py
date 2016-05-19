from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        return self.load_view('/index.html')

    def index_json(self):
        notes_result = self.models['Note'].get_all_notes()
        return self.load_view('partials/_index.html', notes=notes_result['result'])

    def new(self):
        return self.load_view('partials/_new.html')

    def create(self):
        note_result = self.models['Note'].create(request.form)
        flash('created note', 'info')
        return redirect('/notes')

    def update(self, id):
        note_result = self.models['Note'].update(request.form, id)
        flash('updated note', 'info')
        return redirect('/notes')


    def destroy(self, id):
        note_result = self.models['Note'].destroy(id)
        flash('deleted note', 'info')
        return redirect('/notes')

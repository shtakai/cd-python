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
        # print 'Notes#index', request.form
        # notes_result = self.models['Note'].get_all_notes()
        # print 'notes_result', notes_result
        return self.load_view('/index.html')

    def index_json(self):
        print 'Notes#index', request.form
        notes_result = self.models['Note'].get_all_notes()
        print 'notes_result', notes_result
        return self.load_view('partials/_index.html', notes=notes_result['result'])

    def new(self):
        print 'Notes#new', request.form
        return self.load_view('partials/_new.html')

    def create(self):
        print 'Notes#create', request.form
        note_result = self.models['Note'].create(request.form)
        print 'note_result', note_result
        flash('created note', 'info')
        return redirect('/')

    def update(self, id):
        print 'Notes#update', request.form, id
        note_result = self.models['Note'].update(request.form, id)
        print 'note_result', note_result
        flash('updated note', 'info')
        return redirect('/')


    def destroy(self, id):
        print 'Notes#destroy', request.form, id
        note_result = self.models['Note'].destroy(id)
        print 'note_result', note_result
        flash('deleted note', 'info')
        return redirect('/')

    # def create_html(self):
        # print 'Notes#create_html', request.form
        # note_result = self.models['Note'].create(request.form)
        # print 'note_result', note_result
        # return redirect('/')


    # def create(self):
        # print 'Notes#create', request.form
        # self.models['Note'].create(request.form)
        # notes_result = self.models['Note'].get_all_notes()
        # print 'notes_result', notes_result
        # # return note_result
        # return self.load_view('partials/note.html', notes=notes_result['result'])

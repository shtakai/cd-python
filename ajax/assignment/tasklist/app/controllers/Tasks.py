from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Tasks(Controller):
    def __init__(self, action):
        super(Tasks, self).__init__(action)
        self.load_model('Task')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        print 'Tasks#index', request.form
        tasks_result = self.models['Task'].get_all_tasks()
        print 'tasks_result', tasks_result
        return self.load_view('/index.html', tasks=tasks_result['result'])
        # return self.load_view('/index.html')

    def index_json(self):
        tasks_result = self.models['Task'].get_all_tasks()
        return self.load_view('partials/_index.html', tasks=tasks_result['result'])

    def new(self):
        return self.load_view('partials/_new.html')

    def create(self):
        task_result = self.models['Task'].create(request.form)
        flash('created task', 'info')
        return redirect('/')
        # return redirect('/tasks')

    def update(self, id):
        print 'update', request.form, id
        finished = True if request.form.get('finished') else False
        task_result = self.models['Task'].update(request.form, id, finished)
        flash('updated task', 'info')
        return redirect('/')
        # return redirect('/tasks')


    # def destroy(self, id):
        # task_result = self.models['Task'].destroy(id)
        # flash('deleted task', 'info')
        # return redirect('/tasks')

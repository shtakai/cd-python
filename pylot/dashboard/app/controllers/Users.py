from system.core.controller import *
from time import strftime
import datetime
import string
import random

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def sign_in(self):
        return self.load_view('/users/sign_in.html')

    def sign_up(self):
        return self.load_view('/users/sign_up.html')

    def register(self):
        print 'register', request.form
        result = self.models['User'].register(request.form)
        print "-" * 10
        print result
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            return self.load_view('/users/sign_up.html', email=request.form['email'], first_name=request.form['first_name'], last_name=request.form['last_name'], description=request.form['description'])
        flash('User registered')
        return redirect('/login')

    def login(self):
        print '-' * 10
        print 'login', request.form
        result = self.models['User'].login(request.form)
        if not result['status']:
            for error in result['errors']:
                flash(error, 'error')
            return self.load_view('/users/sign_in.html', email=request.form['email'])

        print 'logged in', result
        session['user'] = result['user']
        session['user_name'] = result['user_name']
        session['user_level'] = result['user_level']
        flash('logged in')

        return redirect('/')


    def dashboard_admin(self):
        print '-' * 10
        print 'dashboard_admin', request.form
        print 'user id:', session['user'], 'user_level:', session['user_level']

        result = self.models['User'].get_user_info(session['user'])
        print 'result:', result
        print 'result-user-user_level:', result['user_level']
        print 'session-user_level:', session['user_level']
        if not session['user_level'] or not result or result['user_level'] != session['user_level']:
            flash('disallowed operation')
            return redirect('/')
        users = self.models['User'].get_all_users()
        print 'all users', users
        return self.load_view('users/dashboard_admin.html',users=users['users'])

    def show(self, id):
        result = self.models['User'].get_user(id)
        if not result['status']:
            flash("user not found")
            return redirect('/')
        print 'get user:', result['user']
        return self.load_view('users/show.html', user=result['user'])

    def edit(self, id):
        print '-' * 10
        print 'edit', request.form
        print 'id', id,'user id:', session['user'], 'user_level:', session['user_level']

        result = self.models['User'].get_user_info(session['user'])
        print 'result:', result
        print 'result-user-user_level:', result['user_level']
        print 'session-user_level:', session['user_level']
        if not session['user_level'] or not result or result['user_level'] != session['user_level']:
            flash('disallowed operation')
        result = self.models['User'].get_user(id)
        if not result['status']:
            flash("user not found")
            return redirect('/')
        print 'get user:', result['user']
        return self.load_view('users/edit.html', user=result['user'])


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





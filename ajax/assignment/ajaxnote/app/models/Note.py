from system.core.model import Model
import re
import bcrypt

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all_notes(self):
        print 'Note#get_all_notes'
        query = 'select * from notes order by updated_at desc'
        notes_result = self.db.query_db(query, {})
        print 'notes_result', notes_result
        return {
                'status': True,
                'result': notes_result
                }

    def create(self,req):
        print 'Note#create', req
        print '-------'
        query = 'insert into notes (title, description, created_at, updated_at) values (:title, :description, NOW(), NOW())'
        print '-------'
        values = {
                'title': req['title'],
                'description': req['description']
                }
        print '-------'
        note_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': note_result
                }


    def update(self, req, id):
        print 'Note#update', req, id
        query = 'update notes set title = :title, description = :description, updated_at = NOW() where id = :id'
        values ={
                'title': req['title'],
                'description': req['description'],
                'id': id
                }
        print 'query', query, values
        note_result = self.db.query_db(query, values)
        print 'note_result', note_result
        return {
                'status': True,
                'result': note_result
                }

    def destroy(self, id):
        print 'Note#destroy', id
        query = 'delete from notes where id = :id'
        values = {
                'id': id
                }
        note_result = self.db.query_db(query, values)
        print 'note_result', note_result
        return {
                'status': True,
                'result': note_result
                }

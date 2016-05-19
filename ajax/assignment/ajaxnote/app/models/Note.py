from system.core.model import Model
import re
import bcrypt

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all_notes(self):
        query = 'select * from notes order by updated_at desc'
        notes_result = self.db.query_db(query, {})
        return {
                'status': True,
                'result': notes_result
                }

    def create(self,req):
        query = 'insert into notes (title, description, created_at, updated_at) values (:title, :description, NOW(), NOW())'
        values = {
                'title': req['title'],
                'description': req['description']
                }
        note_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': note_result
                }


    def update(self, req, id):
        query = 'update notes set title = :title, description = :description, updated_at = NOW() where id = :id'
        values ={
                'title': req['title'],
                'description': req['description'],
                'id': id
                }
        note_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': note_result
                }

    def destroy(self, id):
        query = 'delete from notes where id = :id'
        values = {
                'id': id
                }
        note_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': note_result
                }

from system.core.model import Model
import re
import bcrypt

class Task(Model):
    def __init__(self):
        super(Task, self).__init__()

    def get_all_tasks(self):
        query = 'select * from tasks order by updated_at desc'
        tasks_result = self.db.query_db(query, {})
        return {
                'status': True,
                'result': tasks_result
                }

    def create(self,req):
        query = 'insert into tasks (name, finished, created_at, updated_at) values (:name, :finished, NOW(), NOW())'
        values = {
                'name': req['name'],
                'finished': False
                }
        task_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': task_result
                }


    def update(self, req, id, finished):
        print 'Task#update', req, id, finished
        query = 'update tasks set name = :name, finished = :finished, updated_at = NOW() where id = :id'
        print 'query', query
        values = {
                'name': req['name'],
                'finished': finished,
                'id': id
                }
        print 'values', values
        task_result = self.db.query_db(query, values)
        print 'task_result', task_result
        return {
                'status': True,
                'result': task_result
                }

    def destroy(self, id):
        query = 'delete from tasks where id = :id'
        values = {
                'id': id
                }
        task_result = self.db.query_db(query, values)
        return {
                'status': True,
                'result': task_result
                }

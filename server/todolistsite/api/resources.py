from flask import request
from flask_restful import Resource
from todolistsite import db
from todolistsite.models import Task
from datetime import datetime

class TodoList(Resource):
    
    def get(self):

        title = request.args.get('title')

        if title:
            todoList = Task.query.filter_by(title=title)
        else:
            todoList = Task.query.all()

        if todoList:
            return [todo.json() for todo in todoList]
        
        return {'title': None}, 404
    
    def post(self):

        title = request.json['title']
        description = request.json['description']
        due = request.json['due']

        todo = Task(title=title,
                    description=None if not description else description,
                    due=None if not due else datetime.strptime(due, '%Y-%m-%d'))
        
        db.session.add(todo)
        db.session.commit()
        return todo.json()
    
    def put(self):

        target = request.args.get('title')

        title = request.json['title']
        description = request.json['description']
        due = request.json['due']
        done = request.json['done']

        task = Task.query.filter_by(title=target).first()

        if title:
            task.title = title

        if description:
            task.description = description

        if due:
            task.due = datetime.strptime(due, '%Y-%m-%d')

        if done:
            task.done = True if done == 'True' else False

        db.session.commit()

        return {'note': 'update successful',
                'task': task.json()}

    def delete(self):

        title = request.args.get('title')

        todo = Task.query.filter_by(title=title).first()
        if todo:

            db.session.delete(todo)
            db.session.commit()

            return {'note': 'delete successful',
                    'task' : todo.json()}
        
        return {'note': 'delete unsuccessfull'}, 404

class AllTasks(Resource):

    def get(self):
        todoList = Task.query.all()
        return [todo.json() for todo in todoList]
from flask import request
from flask_restful import Resource
from todolistsite import db
from todolistsite.models import Task
from datetime import datetime

class TodoList(Resource):
    
    def get(self):

        title = request.args.get('title')

        todoList = Task.query.filter_by(title=title)

        if todoList:
            return [todo.json() for todo in todoList]
        
        return {'title': None}, 404
    
    def post(self):

        title = request.args.get('title')
        description = request.args.get('description')
        due = request.args.get('due')

        todo = Task(title=title,
                    description=description.replace("_", " "),
                    due=datetime.strptime(due, '%Y-%m-%d'))
        
        db.session.add(todo)
        db.session.commit()
        return todo.json()
    
    def put(self):

        title = request.args.get('title')
        description = request.args.get('description')
        due = request.args.get('due')

        task = Task.query.filter_by(title=title).first()

        if description:
            task.description = description.replace("_", " ")

        if due:
            task.due = datetime.strptime(due, '%Y-%m-%d')

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
import os
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)
#jwt = JWT(app, authenticate, identity)

#parser = reqparse.RequestParser()
#parser.add_argument('title', type=str)
#parser.add_argument('description', type=str, required=False)
#parser.add_argument('due', type=str, required=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    due = db.Column(db.Date)

    def __init__(self, title, description, due):
        self.title = title
        self.description = description
        self.due = due

    def json(self):
        return {
                'title' : self.title,
                'description' : self.description,
                'due' : self.due.isoformat()
                }

class TodoList(Resource):
    
    #@jwt_required()
    def get(self):

        title = request.args.get('title')

        todoList = Task.query.filter_by(title=title)

        if todoList:
            return [todo.json() for todo in todoList]
        
        return {'title': None}, 404
    
    #@jwt_required()
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

    #@jwt_required()
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

    #@jwt_required()
    def get(self):
        todoList = Task.query.all()
        return [todo.json() for todo in todoList]

api.add_resource(TodoList, f'/task')
api.add_resource(AllTasks, f'/tasks')

if __name__=='__main__':
    app.run(debug=True)
import os
from flask import Flask
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
                'due' : self.due
                }

class TodoList(Resource):
    
    #@jwt_required()
    def get(self, title):
        todoList = Task.query.filter_by(title=title)
        if todoList:
            return [todo.json() for todo in todoList]
        return {'title': None}, 404
    
    #@jwt_required()
    def post(self, title, description, due):
        todo = Task(title=title, description=description, due=due)
        db.session.add(todo)
        db.session.commit()
        return todo.json()

    #@jwt_required()
    def delete(self, title):
        todo = Task.query.filter_by(title=title).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return {'note': 'delete successful',
                'task' : todo.json()}

class AllTasks(Resource):

    #@jwt_required()
    def get(self):
        todoList = Task.query.all()
        return [todo.json() for todo in todoList]

api.add_resource(TodoList, f'/task/<string:title>')
api.add_resource(AllTasks, f'/tasks')

if __name__=='__main__':
    app.run(debug=True)
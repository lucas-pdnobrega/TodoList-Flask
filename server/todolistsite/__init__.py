import os
from flask import Flask
from flask_restful import Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

# SETTING UP DATABASE
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SETTING UP CROSS ORIGIN
cors = CORS(app, resources={"/tasks": {"origins": "http://localhost:5173"},
                            "/task": {"origins": "http://localhost:5173"}})

db = SQLAlchemy(app)
Migrate(app, db)

from todolistsite.api.resources import TodoList, AllTasks

# SETTING UP API
api = Api(app)
api.add_resource(TodoList, f'/task')
api.add_resource(AllTasks, f'/tasks')
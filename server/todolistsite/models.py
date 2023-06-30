from datetime import datetime
from todolistsite import db

class Task(db.Model):

    __tablename__ = "Task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    due = db.Column(db.Date, default=datetime.now())
    done = db.Column(db.Boolean, default=False)

    def __init__(self, title, description = None, due = None):
        self.title = title
        if description:
            self.description = description
        if due:
            self.due = due

    def json(self):
        return {
                'id' : self.id,
                'title' : self.title,
                'description' : self.description,
                'due' : self.due.isoformat(),
                'done' : self.done
                }
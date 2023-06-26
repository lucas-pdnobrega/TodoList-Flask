from todolistsite import db

class Task(db.Model):

    __tablename__ = "Task"
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
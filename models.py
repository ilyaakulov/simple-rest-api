from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String())

    def __init__(self, subject):
        self.subject = subject

    def __repr__(self):
        return '<id {}>'.format(self.id)

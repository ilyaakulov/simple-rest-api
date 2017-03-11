from app import app, db
from models import Task
from json import dumps
from sqlalchemy.orm import class_mapper
from flask import request


def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]
    # then we return their values in a dict
    return dict((c, getattr(model, c)) for c in columns)


@app.route('/put', methods=['GET', 'POST', ])
def add_row():
    table = request.args.get('table')
    if table.lower() == 'task':
        subject = request.args.get('subject')
        task = Task(subject=subject)
        db.session.add(task)
        db.session.commit()
        return "Task '{}' added to tasks!".format(subject)
    return "Unknown table {}!".format(table)


@app.route('/get', methods=['GET', 'POST', ])
def get_tasks():
    serialized_labels = [
        serialize(label)
        for label in db.session.query(Task).all()
        ]
    json = dumps(serialized_labels)
    return json

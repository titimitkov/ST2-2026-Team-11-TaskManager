from models.task import Task
from extensions import db


class TaskRepository:
    """
    Repository Pattern.

    Този клас е отговорен за достъпа до базата данни
    за обектите от тип Task.
    """

    def get_all(self):
        return Task.query.all()

    def get_by_id(self, task_id):
        return db.session.get(Task, task_id)

    def create(self, task):
        db.session.add(task)
        db.session.commit()
        return task

    def update(self, task):
        db.session.commit()
        return task

    def delete(self, task):
        db.session.delete(task)
        db.session.commit()
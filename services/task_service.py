from models.task import Task
from repositories.task_repository import TaskRepository


class TaskService:
    """
    Service Layer Pattern.

    Този клас съдържа бизнес логиката за задачите.
    Той използва Repository за работа с базата данни.
    """

    def __init__(self):
        self.repository = TaskRepository()

    def get_all_tasks(self):
        return self.repository.get_all()

    def get_task(self, task_id):
        return self.repository.get_by_id(task_id)

    def create_task(self, title, description):
        task = Task(
            title=title,
            description=description,
            status="pending"
        )

        return self.repository.create(task)

    def update_task(self, task, title, description, status):
        task.title = title
        task.description = description
        task.status = status

        return self.repository.update(task)

    def delete_task(self, task):
        self.repository.delete(task)
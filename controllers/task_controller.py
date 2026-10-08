from flask import Blueprint, redirect, render_template, request, url_for

from services.task_service import TaskService


task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

task_service = TaskService()


@task_bp.route("/")
def list_tasks():
    tasks = task_service.get_all_tasks()

    return render_template(
        "tasks.html",
        tasks=tasks
    )


@task_bp.route("/create", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        task_service.create_task(
            title=title,
            description=description
        )

        return redirect(url_for("tasks.list_tasks"))

    return render_template("task_create.html")


@task_bp.route("/<int:task_id>")
def task_details(task_id):
    task = task_service.get_task(task_id)

    if task is None:
        return "Task not found", 404

    return render_template(
        "task_details.html",
        task=task
    )


@task_bp.route("/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = task_service.get_task(task_id)

    if task is None:
        return "Task not found", 404

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        status = request.form.get("status")

        task_service.update_task(
            task=task,
            title=title,
            description=description,
            status=status
        )

        return redirect(
            url_for("tasks.task_details", task_id=task.id)
        )

    return render_template(
        "task_edit.html",
        task=task
    )


@task_bp.route("/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = task_service.get_task(task_id)

    if task is None:
        return "Task not found", 404

    task_service.delete_task(task)

    return redirect(url_for("tasks.list_tasks"))
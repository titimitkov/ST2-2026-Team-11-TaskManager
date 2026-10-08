from flask import Blueprint, render_template, request

from services.ai_service import AIService
from services.ollama_provider import OllamaProvider
from services.task_service import TaskService


ai_bp = Blueprint(
    "ai",
    __name__,
    url_prefix="/ai"
)


ai_service = AIService(
    OllamaProvider()
)

task_service = TaskService()


@ai_bp.route("/", methods=["GET", "POST"])
def ai_assistant():

    task_id = request.args.get("task_id", type=int)

    prompt = ""
    answer = None
    error = None
    task = None

    if task_id is not None:
        task = task_service.get_task(task_id)

        if task is None:
            return "Task not found", 404

    if request.method == "POST":

        prompt = request.form.get("prompt", "").strip()

        if prompt:

            try:

                if task is not None:
                    full_prompt = (
                        "Отговаряй на български език.\n"
                        "Отговори директно и конкретно на въпроса.\n"
                        "Не измисляй думи и не променяй смисъла на въпроса.\n\n"
                        "Информация за задачата:\n"
                        f"Заглавие: {task.title}\n"
                        f"Описание: {task.description or 'Няма описание.'}\n"
                        f"Статус: {task.status}\n\n"
                        f"Въпрос на потребителя: {prompt}\n\n"
                        "Дай ясен и полезен отговор."
                    )

                else:
                    full_prompt = prompt

                answer = ai_service.ask(full_prompt)

            except Exception:
                error = (
                    "Възникна грешка при комуникацията "
                    "с локалния AI модел."
                )

    return render_template(
        "ai.html",
        prompt=prompt,
        answer=answer,
        error=error,
        task=task
    )
# Task Manager

Уеб приложение за управление на задачи, разработено с Python и Flask.

Проектът демонстрира MVC архитектура, работа с база данни, CRUD операции, Design Patterns и комуникация с локален езиков модел чрез Ollama.

## Технологии

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Ollama
- HTML
- CSS
- Jinja2
- Git и GitHub

## Основни функционалности

Приложението позволява:

- създаване на задачи;
- преглеждане на всички задачи;
- преглеждане на детайли за конкретна задача;
- редактиране на задачи;
- изтриване на задачи;
- промяна на статуса на задача;
- използване на локален AI асистент;
- задаване на въпроси към AI относно конкретна задача.

## Архитектура

Проектът използва MVC архитектура:

### Model

Моделът описва структурата на данните и връзката с базата данни.

Основният модел е:

```text
models/task.py
```

Той съдържа:

- `id`
- `title`
- `description`
- `status`
- `created_at`

### View

View частта е реализирана чрез Flask templates и Jinja2.

Основните views са:

```text
templates/index.html
templates/tasks.html
templates/task_create.html
templates/task_edit.html
templates/task_details.html
templates/ai.html
```

### Controller

Controller частта обработва HTTP заявките и свързва Views със Service Layer.

Основните controllers са:

```text
controllers/task_controller.py
controllers/ai_controller.py
```

## Design Patterns

В проекта са реализирани няколко Design Patterns.

### 1. Repository Pattern

Файл:

```text
repositories/task_repository.py
```

`TaskRepository` отговаря за операциите към базата данни.

Той реализира операции като:

- извличане на всички задачи;
- извличане на задача по ID;
- създаване;
- update;
- delete.

По този начин логиката за достъп до базата данни е отделена от бизнес логиката.

### 2. Service Layer Pattern

Файл:

```text
services/task_service.py
```

`TaskService` съдържа бизнес логиката за работа със задачите.

Controller-ите не работят директно с базата данни, а използват Service Layer.

Това разделя отговорностите между различните части на приложението.

### 3. Application Factory Pattern

Файл:

```text
app.py
```

Функцията:

```python
create_app()
```

създава и конфигурира Flask приложението.

В нея се:

- зарежда конфигурацията;
- инициализира базата данни;
- регистрират се Blueprint-ите.

Този подход улеснява тестването и разширяването на приложението.

### 4. Strategy Pattern

Файлове:

```text
services/ai_provider.py
services/ollama_provider.py
services/ai_service.py
```

AI комуникацията използва Strategy Pattern.

`AIProvider` дефинира общ интерфейс за AI доставчик.

`OllamaProvider` е конкретна стратегия, която комуникира с локален Ollama модел.

Така в бъдеще може да бъде добавен друг AI provider, без да се променя основната логика на `AIService`.

## CRUD операции

Приложението реализира пълни CRUD операции върху задачите.

### Create

Потребителят може да създава нова задача от:

```text
/tasks/create
```

### Read

Всички задачи могат да бъдат преглеждани от:

```text
/tasks/
```

Конкретна задача може да бъде преглеждана от:

```text
/tasks/<id>
```

### Update

Задача може да бъде редактирана от:

```text
/tasks/<id>/edit
```

### Delete

Задача може да бъде изтрита от:

```text
/tasks/<id>/delete
```

## База данни

Приложението използва SQLite.

Файлът на базата данни е:

```text
database/app.db
```

SQLAlchemy се използва като ORM за работа с базата данни.

Основната таблица е:

```text
tasks
```

## AI функционалност

Приложението комуникира с локален езиков модел чрез Ollama.

Използваният модел е:

```text
llama3.2:3b
```

Ollama работи локално на:

```text
http://localhost:11434
```

AI асистентът може да работи самостоятелно или с контекст на конкретна задача.

При използване от страницата на задача AI получава информация за:

- заглавието;
- описанието;
- статуса.

След това потребителят може да зададе въпрос, свързан със задачата.

## Структура на проекта

```text
ST2-2026-Team-11-TaskManager/
│
├── app.py
├── extensions.py
├── requirements.txt
│
├── config/
│   └── config.py
│
├── models/
│   ├── __init__.py
│   └── task.py
│
├── views/
│   ├── __init__.py
│   └── home.py
│
├── controllers/
│   ├── __init__.py
│   ├── task_controller.py
│   └── ai_controller.py
│
├── services/
│   ├── task_service.py
│   ├── ai_provider.py
│   ├── ollama_provider.py
│   └── ai_service.py
│
├── repositories/
│   └── task_repository.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── tasks.html
│   ├── task_create.html
│   ├── task_edit.html
│   ├── task_details.html
│   └── ai.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── database/
│   └── app.db
│
└── .gitignore
```

## Инсталация

### 1. Клониране на проекта

```bash
git clone https://github.com/titimitkov/ST2-2026-Team-11-TaskManager.git
```

След това:

```bash
cd ST2-2026-Team-11-TaskManager
```

### 2. Създаване на виртуална среда

```bash
python3 -m venv venv
```

### 3. Активиране на виртуалната среда

На macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Инсталиране на зависимостите

```bash
pip install -r requirements.txt
```

## Настройване на базата данни

Стартирайте
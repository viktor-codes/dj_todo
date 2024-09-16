# ToDo Web Application

The ToDo Web Application is a simple and efficient task management system built using Django. This project allows users to create, view, update, and delete tasks, as well as toggle their completion status. Additionally, tasks can be associated with tags for better organization.

## Features

- **Task Management:** Create, view, update, and delete tasks easily.
- **Sorting:** Tasks are displayed based on completion status and creation time.
- **Tagging:** Associate tasks with tags for better organization and categorization.
- **User-Friendly Interface:** The project provides a clean and intuitive user interface for efficient task management.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/viktor-codes/dj_todo.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Create a task by visiting the homepage and clicking on "New Task."
2. View and manage tasks on the task list page, where tasks are sorted by completion status and creation time.
3. Edit or delete tasks by clicking on the respective options in the task detail view.
4. Associate tags with tasks for better organization on the tag list page.

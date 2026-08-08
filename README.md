# Flask Todo App

## 1. Project Overview
Flask Todo App is a lightweight Flask web application for registering users, logging in, and managing personal todo tasks. Each authenticated user works with their own task list backed by SQLite.

## 2. Features
- User registration
- User login and logout
- Session-based authentication
- User-specific todo lists
- Add new tasks
- Move task status through Pending, Working, and Done
- Delete individual tasks
- Clear all tasks for the logged-in user
- Flash messages for user feedback

## 3. Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- JavaScript

## 4. Authentication
The app uses Flask sessions to keep track of the logged-in user. After a successful login, the app stores the user id and username in the session and uses that session data to protect the task dashboard.

## 5. User-specific Todo Tasks
Tasks are tied to the authenticated user. When a user logs in, they only see, update, and delete their own tasks.

## 6. Task Management
The app supports creating tasks, updating task status, deleting a single task, and clearing all tasks for the current user. Task status cycles through Pending, Working, and Done.

## 7. Project Structure
```text
TODO_APP/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── tasks.html
│   ├── __init__.py
│   └── models.py
├── .gitignore
├── requirements.txt
└── run.py
```

## 8. Installation
Clone the repository and move into the project folder.

```bash
git clone https://github.com/shashi9094/flask-todo-app.git
cd flask-todo-app
```

## 9. Virtual Environment Setup
Create and activate a virtual environment on Windows.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 10. Installing Dependencies
Install the required Python packages.

```bash
pip install -r requirements.txt
```

## 11. Running the Application
Start the Flask application with:

```bash
python run.py
```

Then open the app in your browser at:

```text
http://127.0.0.1:5000
```

## 12. Future Improvements
- Hash passwords before storing them
- Add CSRF protection for forms
- Add task edit functionality
- Add form validation and better error handling
- Add automated tests
- Add deployment instructions for production hosting
- Add database migrations
- Add screenshots to this README

## 13. Screenshots
Screenshots are not included yet.

- Login page: add a screenshot here later
- Tasks dashboard: add a screenshot here later

## 14. Author
Shashi Kumar Singh

## 15. License
No license has been added yet. Add one before publishing the project publicly.

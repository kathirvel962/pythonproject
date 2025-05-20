# E-Learning Portal for Coding

A simple Django-based e-learning platform for coding education.

## Features
- Interactive coding exercises
- Course management (add/delete courses)
- Course completion progress tracking
- Multiple programming language support
- User-friendly interface

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Admin Access
- Visit http://127.0.0.1:8000/admin to access the admin panel
- Login with your superuser credentials
- Manage courses, users, and content 
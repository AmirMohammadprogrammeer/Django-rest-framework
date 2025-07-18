blog api

📰 Blog API with JWT Authentication

This is a simple blog backend built with **Django** and **Django REST Framework**, featuring:

- JWT-based authentication (register / login / refresh tokens)
- User registration & login system
- Authenticated users can create blog posts
- Only authenticated users can post content
- Author field is automatically set from the request user
- Permissions and access control enforced
- Clean, scalable API structure (Class-Based Views)

📦 Tech Stack
Python 3.8+
Django 4.x
Django REST Framework
Simple JWT
SQLite3 (default database)

🚀 Features
✅ JWT Auth (access + refresh)
✅ User Register / Login
✅ Authenticated Post Creation
✅ Automatic author assignment
✅ Permissions (only authenticated users can write)

JWT Authentication
Register:
POST /api/auth/register/

Fields:

username

first_name

last_name

password

password_confirmation

🔒 Secure API structure

🔧 Installation & Setup 

```bash

git clone https://github.com/YourUsername/your-repo-name.git](https://github.com/AmirMohammadprogrammeer/Django-rest-framework
cd your-repo-name
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

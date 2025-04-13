# 💬 Secure Link Chat Backend

This is the **backend** for a modular chat application built using Django and Django Channels (WebSockets). It supports features like user registration, login with phrase validation, private chat, file upload, and auto-clearing chats on logout. The backend is designed to communicate with a React frontend via APIs only.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **Django 4.2**
- **Django Channels** (for WebSocket support)
- **PostgreSQL** (as the database)
- **Daphne** (ASGI server for WebSockets)
- **Pillow** (image handling)
- **Gunicorn** (for production deployment)
- **django-cors-headers** (for frontend communication)

---

## 📦 Requirements

Before running the project, install dependencies using:

```bash
pip install -r requirements.txt
```

To create the `venv` (virtual environment):

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

---

## 🛠️ Project Structure

```
secure-link-backend/
│
├── chat/                   # Main chat app
│   ├── consumers.py        # WebSocket handlers
│   ├── models.py           # User, Message models
│   ├── routing.py          # WebSocket URL routing
│   ├── views.py            # API views for login, register, etc.
│   └── ...
│
├── media/                  # Uploaded files (profile pics, chat files)
├── secure_link_backend/    # Main Django config (ASGI, settings, etc.)
├── db.sqlite3              # SQLite DB (or connect to PostgreSQL)
├── manage.py               # Django command-line utility
└── requirements.txt        # Python dependencies
```

---

## 🔧 Setting Up PostgreSQL

Make sure PostgreSQL is installed. Create a database and update your `settings.py` like:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📡 Running the Project Locally

Start the development server (with WebSockets):

```bash
# Run with ASGI server
daphne secure_link_backend.asgi:application
```

Or:

```bash
# With built-in dev server (for basic API testing)
python manage.py runserver
```

---

## 🔌 WebSocket Connection

Connect to WebSocket using:

```
ws://localhost:8000/ws/chat/
```

Use frontend (JavaScript or React) to initiate WebSocket connection.

---

## 📤 API Endpoints

| Endpoint                | Method | Description                  |
|-------------------------|--------|------------------------------|
| `/api/register/`        | POST   | Register new user            |
| `/api/login/`           | POST   | Login with username + phrase |
| `/api/logout/`          | POST   | Logout user and clear chat   |
| `/api/upload-file/`     | POST   | Upload chat attachments      |
| `/api/send-message/`    | POST   | Send message (REST fallback) |
| `/api/user-profile/`    | GET    | Get logged-in user info      |

---

## 📁 File Uploads

All uploaded files (profile pictures, chat attachments) are stored in the `media/` directory and accessible via:

```
http://localhost:8000/media/<filename>
```

---

## 🧪 Testing Locally with Browser

Use browser console to test WebSocket:

```js
const socket = new WebSocket("ws://localhost:8000/ws/chat/");

socket.onopen = () => {
  console.log("WebSocket connected!");
  socket.send(JSON.stringify({ type: "chat", message: "Hello from browser!" }));
};

socket.onmessage = (event) => {
  console.log("Message received: ", event.data);
};
```

---

## 👨‍💻 Version Control

This project uses **GitHub** for version control. Don't forget to:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

---

## 🧹 .gitignore

Make sure `.gitignore` is included to avoid pushing unnecessary files:

```
__pycache__/
*.pyc
*.sqlite3
media/
.env
venv/
.idea/
.vscode/
```

---

## 📌 Deployment

You can use **Railway**, **Render**, or **Heroku** to deploy the backend for free (serving up to 10–50 users). Gunicorn + Daphne is recommended for production.

---

## 🙋 Questions?

If you're using this project, feel free to fork it or raise issues for help! This backend is designed to work with a modular React frontend (coming soon 🚀).

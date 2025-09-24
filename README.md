🎬 Movie Recommendation App (Backend)
📌 Overview

This project is a Django REST API backend for a movie recommendation application.
It integrates with PostgreSQL for data storage and uses Redis (planned) for caching trending and recommended movies.

The backend provides:

APIs for fetching trending and recommended movies (via TMDb API).

JWT-based authentication for secure user access.

User preferences (saving favorite movies).

API documentation with Swagger.

This project mirrors real-world backend development by focusing on:

Performance optimization.

Security (JWT authentication).

Industry best practices.

Clear documentation for frontend integration.

🛠️ Tech Stack

Backend Framework: Django + Django REST Framework (DRF)

Database: PostgreSQL

Caching: Redis (for performance optimization)

Authentication: JWT (JSON Web Tokens)

API Docs: Swagger (drf-yasg)

External API: TMDb (The Movie Database API)

📊 ERD (Entity Relationship Diagram)

The database schema is designed to manage users, movies, and user preferences efficiently.

(replace the link above with your ERD from draw.io or Lucidchart export)

🚀 Setup Instructions
1️⃣ Clone the repo
git clone git@github.com:y123-cmd/movie-recommendation-app.git
cd movie-recommendation-app

2️⃣ Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Update movie_app/settings.py with your database credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_db',
        'USER': 'movie_user',
        'PASSWORD': 'Yvonneboss@88',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

5️⃣ Run migrations
python manage.py migrate

6️⃣ Start the server
python manage.py runserver

🔑 Features

Movie Recommendations:
Fetch trending and recommended movies from TMDb API.

User Authentication:
Secure login/signup with JWT.

User Preferences:
Save, update, and fetch favorite movies.

Performance Optimization:
Redis caching to reduce API calls.

API Documentation:
Swagger UI hosted at /api/docs.

📹 Deliverables (for presentation)

ERD Diagram – Google Doc link

Slides – Google Slides presentation

Demo Video – < 5 minutes project walkthrough

Hosted API – (Heroku/Render link will be added after deployment)

👨‍💻 Author

Yvonne Bosire
Backend Developer | Django Enthusiast

GitHub: y123-cmd

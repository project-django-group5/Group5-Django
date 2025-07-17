# About SkillSwap

SkillSwap is a Django-based web platform where users can connect by offering or requesting skills — from music lessons and cooking to tutoring or learning a new language. The platform facilitates user interactions, messaging, and reviews, simulating a community-driven skill-sharing marketplace.

## Demo



## 💻 How to Install & Run Locally

- Clone the repository:
  - *git clone https://github.com/yourusername/skillswap.git*  
  - *cd skillswap*
- Create and activate a virtual environment:
  - *python -m venv env*
  - *source env/bin/activate*  # On Windows: env\Scripts\activate
- Install dependencies:
  - *pip install -r requirements.txt*
- Run migrations:
  - *python manage.py makemigrations*
  - *python manage.py migrate*
- Create a superuser (optional, for admin access):
  - *python manage.py createsuperuser*
- Run the development server:
  - *python manage.py runserver*
- Visit the app:
  - Open your browser and go to: http://127.0.0.1:8000/

## ✨ Features Implemented

#### 1. 🔐 User Authentication

* Signup / Login / Logout
* Profile creation & editing (bio, profile picture optional)

#### 2.📋 Skill Listings
* Post a skill to offer or request
* Each skill includes:
    * Title, category, description
    * Availability (e.g., evenings/weekends)
    * Location (optional)
🔍 Search & Browse
* Browse all skills
* Filter by:
    * Skill type (offered/requested)
    * Category (e.g., Arts, Tech, Language)
✉️ Contact / Messaging
* "Contact" button opens a simple form to send a message
* Simulated inbox for communication
⭐ Reviews & Ratings
* After a session, users can leave:
    * 1–5 star rating
    * A short review
🧰 Optional Features (Implemented)
* Profile pictures
* Admin dashboard
* Skill categories/tags

🛠 Tech Stack
* Backend: Django (Python)
* Frontend: HTML, CSS, Bootstrap 4.6
* Database: SQLite (default, for development)
    * Other: Django Admin, Django Messages Framework




https://github.com/user-attachments/assets/9445296b-c348-49ca-97e0-a0f2e54b33cf

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

#### 2. 📋 Skill Listings

* Post a skill to offer or request
* Each skill includes:
    * *Title, category, description*
    * *Availability (e.g., evenings/weekends)*
    * *Location (optional)*
  
#### 3. 🔍 Search & Browse

* Browse all skills
* Filter by:
    * *Skill type (offered/requested)*
    * *Category (e.g., Arts, Tech, Language)*
  
#### 4. ✉️ Contact / Messaging

* "Contact" button opens a simple form to send a message
  
#### 5. ⭐ Reviews & Ratings

* After a session, users can leave:
    * *1–5 star rating*
    * *A short review*
  
#### 🧰 Optional Features (Implemented)
* *Profile pictures*
* *Admin dashboard*


### 🛠 Tech Stack
***
* **Backend**: *Django (Python)*
* **Frontend**: *HTML, CSS, Bootstrap 4.6*
* **Database**: *SQLite (default, for development)*
    * **Other**: *Django Admin*

### 👥 Team Members
***
* Ayisha Ameer
* Elaiyarani Soundararajan
* Judith Soundarya Joseph
* Kanimozhi Sangapillai
* Sowmya Ayarottupura Velayudhankutty

#### 📌 Project Management
---
    We used Agile methodology with weekly iterations and task tracking using Trello. 

🔗 [*SkillSwap TrelloBoard*](https://trello.com/invite/b/686e2b4c901ef0a5cd293f61/ATTIfea069f3de442e18869a05bb6983898494E020FC/skillswap)

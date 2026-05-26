**🎬 Movie Ticket Booking System**
A Django-based web application for online movie ticket booking with seat selection and admin management.

**Feature**
🎥 View available movies
💺 Seat selection system
🧾 Booking summary page
👤 User authentication (login/register)
  Admin panel to manage movies & bookings
📧 Email confirmation (if added)

**Tech Stack**
Python (Django)
HTML, CSS, JavaScript
SQLite Database
Bootstrap
**📁 Project Structure**
Movie-Ticket-booking-system/
│
├── Book/
├── customer/
├── user_authentication/
├── templates/
├── static/
├── db.sqlite3
├── manage.py

**How to Run Locally**
# Clone repository
git clone https://github.com/Gahana19/Movie-Ticket-booking-system.git

# Go to project folder
cd Movie-Ticket-booking-system

# Create virtual environment
python -m venv venv

# Activate venv (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

**👨‍💻 Developer**
Gahana Pokhrel | Student Project

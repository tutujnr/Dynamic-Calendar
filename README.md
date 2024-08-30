# Dynamic Calendar Application
# Overview
This project involves developing a dynamic calendar application using FastAPI, MongoDB, and Vite.js. The application will support day, week, and month views and allow users to create, manage, and view scheduled meetings and tasks seamlessly.

# Features
Day, Week, and Month Views: Switch between different calendar views to see your schedule in various formats.

Create and Manage Events: Add, edit, and delete meetings and tasks.

View Scheduled Events: Easily view your upcoming and past events.

# Technologies
FastAPI: For building the backend API.

MongoDB: To store and manage calendar data.

Vite.js: For a fast and modern frontend development environment.

# Installation
Clone the Repository

git clone https://github.com/tutujnr/Dynamic-Calendar.git

cd calendar-app

Backend Setup

Navigate to the backend directory.

# Install dependencies:

pip install -r requirements.txt

Set up your MongoDB connection in config.py.

# Run the FastAPI server:

uvicorn main:app --reload
Frontend Setup

# Start the development server:
npm run dev

# API Endpoints

GET /api/events: Retrieve a list of scheduled events.

POST /api/events: Create a new event.

PUT /api/events/{id}: Update an existing event.

DELETE /api/events/{id}: Delete an event.

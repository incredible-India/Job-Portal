# Job Portal App

## Overview

The **Job Portal App** is a web-based application that allows users to browse, apply for jobs, and manage their profiles. Users can register, update their details, and apply for jobs. Employers can post job listings, and users can view job details and apply to those that fit their qualifications.

## Features

- **User Registration & Authentication**
  - Users can sign up, log in, and log out.
  - Profile management: Users can update personal information, upload a profile image, and change contact details.
  
- **Job Listings**
  - Employers can post jobs, including job title, description, salary, and other details.
  - Users can browse available jobs, see job details, and apply for jobs.

- **Job Application**
  - Users can apply for jobs and view jobs they've already applied for.
  
- **Responsive Design**
  - The app is fully responsive, so users can access it on any device (mobile, tablet, desktop).

## Technologies Used

- **Django** - Python-based web framework for building the backend and API.
- **Bootstrap** - Used for styling and responsive design.
- **SQLite** (or PostgreSQL/MySQL) - Database for storing user and job-related data.
- **HTML/CSS/JavaScript** - Used for frontend design and functionality.

## Setup Instructions

Follow these steps to get the application running locally.

### 1.open cmd or powershell Clone the Repository

```bash
git clone https://github.com/incredible-India/Job-Portal.git
cd job-portal
```
### 2. Locate the directory where manage.py file is there in same directory open powershell or cmd
### 3. make sure Django and python is install in your local machine
### 4. if django is not install then cmd/powershell type the follwing command
```bash
pip install django
```
### 5. Once django install then write the follwing command (where manage.py is there) in cmd/powershell
```bash
python .\manage.py makemigrations

then
python .\manage.py migrate

in last

python .\manage.py runserver

```

### 6. Default it will run on port 8000
### 7. open browser and type in url  http://127.0.0.1:8000/
### 8. to see the admin control http://127.0.0.1:8000/admin  
### 9. username is myjob and password is myjob

### 10. Feel free to contact me if any issue is still there 8604470501





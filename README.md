
# CV Builder Project

## Overview
The CV Builder project is a Django REST framework-based application that allows users to register, log in, and create and manage their CVs. The system allows users to provide details such as bio, skills, job experience, education, and certificates. Additionally, users can download their CV in PDF format.

## Features
- **User Registration & Authentication**: Users can register and log in using JWT tokens or session-based authentication.
- **Profile Management**: Users can manage their profiles, including adding skills, job experience, education, and certificates.
- **Download CV as PDF**: Users can download their profile details in a PDF format, making it easy to share or print their CV.
- **Swagger Documentation**: The project includes Swagger for API documentation, making it easier to test and explore the available endpoints.

## Installation

### Prerequisites
- Python 3.x
- Django 3.2.x
- Django REST Framework
- PostgreSQL (for database)
- djangorestframework-simplejwt
- drf-yasg (for Swagger API documentation)


### Install Dependencies
1. Clone the repository:
   ```bash
   git clone https://github.com/PeymanNr/django-cv-builder.git
   cd cv-builder
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

### Environment Variables
Ensure the following environment variables are set in a `.env` file:
- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `False` for development.
- `DB_NAME`: Database name.
- `DB_USER`: Database username.
- `DB_PASSWORD`: Database password.
- `DB_HOST`: Database host (e.g., `localhost`).
- `DB_PORT`: Database port (default: `5432`).

## Usage

### Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### API Endpoints

- **POST `/user/register/`**: Register a new user.
- **POST `/user/login/`**: Log in and get a JWT token for authentication.
- **GET `/user/profile/`**: Get the user's profile.
- **PUT `/user/profile/`**: Update the user's profile.
- **POST `/user/profile/skills/`**: Add skills to the user's profile.
- **GET `/user/profile/pdf/`**: Download the user's profile as a PDF.

### Example Request to Download Profile as PDF
To download your profile as a PDF, make a `GET` request to the following endpoint:
```bash
GET /user/profile/pdf/
```
This will generate a PDF file with your profile details that can be downloaded.

### API Documentation
The project includes Swagger for API documentation. You can access it by navigating to:
```
http://localhost:8000/docs/
```

## Testing
The project includes automated tests to ensure the functionality is working correctly. To run the tests, use the following command:
```bash
python manage.py test
```

## Deployment

### Prepare for Production
To deploy the project to production, you can use services like Heroku, AWS, or any other platform supporting Django. Make sure to set `DEBUG = False` in the production environment, configure the database, and set the proper environment variables.

## Dependencies
- `Django 3.2.x`: Web framework for building the application.
- `Django REST Framework`: For building RESTful APIs.
- `ReportLab`: For generating PDF files.
- `djangorestframework-simplejwt`: For JWT authentication.

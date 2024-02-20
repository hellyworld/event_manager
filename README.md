_For original instruction check [INSTRUCTIONS.md](INSTRUCTIONS.md)_

# Event Manager API

The Event Manager API is a Django REST Framework project designed to facilitate the creation, management, and
registration of events. It allows users to create personal accounts, log in, create and edit events, and register to
attend events. This project adheres to clean coding practices, using modern Python development tools and methodologies.

## Features

- User account registration and authentication
- JWT-based token authentication with access and refresh tokens
- Event creation, listing, and editing
- Registration for future events by authenticated users
- Filtering events by various criteria (to be implemented)

## Prerequisites

- Python 3.12
- Pip and Virtualenv
- Git (for version control)

## Installation

Clone the project repository:

```bash
git clone <repository-url>
cd core
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

## Setup

### Environment Variables

Create a `.env` file in the project root directory and add the following variables:

```plaintext
DEBUG=1
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=.localhost, .127.0.0.1
```

### Database Migrations

Apply database migrations to set up your database schema:

```bash
python manage.py migrate
```

### Create Superuser

Create an admin user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

### Run Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### API Documentation

#### DRF Spectacular Auto-generated Docs

To explore and test endpoints, navigate to `/schema/docs` in your browser with the development server running.

#### Using Provided `.rest` Files

The project includes `.rest` files for testing API endpoints directly within Visual Studio Code using the REST Client
extension. This approach allows you to easily send HTTP requests and view responses without leaving your editor.

**Prerequisites:**

- Ensure you have Visual Studio Code installed.
- Install the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) in Visual
  Studio Code.

**To Use `.rest` Files for Testing:**

- Open the provided `.rest` file (e.g., `test_api.rest`) in Visual Studio Code.
- You'll see "Send Request" links above each HTTP request. Click on these links to execute the requests and view
  responses directly within VS Code.

This method provides a convenient way to interact with the API, making it easy to test different endpoints as you
develop and debug your application.

## Running the Tests

Use pytest to execute automated tests and pytest-cov for coverage reports. Here's how to get started:

Running all tests

```bash
pytest
```

To generate a coverage report:

```bash
pytest --cov
```

Generate an HTML coverage report with:

```bash
coverage html
```

The report is saved in htmlcov/index.html. Open it in a browser to view detailed coverage information.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs
* [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/) - Schema generation for Django REST Framework

## Future Enhancements

### Admin Dashboard

A graphical interface for admins to manage events, users, and view system statistics.

### Enhanced Logging System

A flexible logging system to capture and store logs using file systems, databases, or services
like Sentry for easier monitoring and troubleshooting.

### Refresh Token Authentication

Implement refresh tokens for longer session management, reducing the need for frequent logins
by securely refreshing access tokens.

### Event Recommendations

A feature suggesting events to users based on their interests and past activities,
leveraging user data and preferences.

### Push Notifications

Notifications for upcoming events, updates, and personalized alerts to keep users engaged,
using technologies like web sockets or Firebase Cloud Messaging.

### User Feedback and Ratings

Enable users to rate events and provide feedback, helping
organizers improve event quality and engagement.

_For original instruction check [INSTRUCTIONS.md](INSTRUCTIONS.md)_
# Event Manager API

The Event Manager API is a Django REST Framework project designed to facilitate the creation, management, and registration of events. It allows users to create personal accounts, log in, create and edit events, and register to attend events. This project adheres to clean coding practices, using modern Python development tools and methodologies.

## Features

- User account registration and authentication
- JWT-based token authentication with access and refresh tokens
- Event creation, listing, and editing
- Registration for future events by authenticated users
- Filtering events by various criteria (to be implemented)

## Prerequisites

- Python 3.8 or newer
- Pip and Virtualenv
- Git (for version control)

## Installation

Clone the project repository:

```bash
git clone <repository-url>
cd event_manager
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

## Usage

This section should include examples of how to use the API, such as making requests to create an account, log in, and create an event. (This will be filled in with specific examples of API requests and responses.)

## Running the Tests

Explain how to run the automated tests for this system. (Instructions to be completed.)

## Deployment

Provide basic guidelines on deploying the project to a live system. (To be completed based on the deployment method chosen.)

## Contributing

We welcome contributions to the Event Manager API! For more information on how to contribute, please refer to our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used as inspiration.
- Additional acknowledgments and credits. (To be filled in.)
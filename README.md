# Django User CRUD App

This Django app provides a simple CRUD (Create, Read, Update, Delete) interface for managing user information. The app is containerized using Docker, and it uses PostgreSQL as the database.

## Getting Started

These instructions will help you set up and run the Django app locally.

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-user-crud-app.git
Change into the project directory:

bash
Copy code
cd django-user-crud-app
Build the Docker image:

bash
Copy code
docker-compose build
Run the Docker containers:

bash
Copy code
docker-compose up
The Django app will be accessible at http://localhost:8000/

Create initial database migrations:

bash
Copy code
docker-compose exec djangoapp python manage.py migrate
API Endpoints
Create User:

Method: POST

URL: http://localhost:8000/users/create

Request Body:

json
Copy code
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "age": 25
}
Read Users:

Method: GET
URL: http://localhost:8000/users/
Update User:

Method: PUT

URL: http://localhost:8000/users/<user_id>/

Request Body:

json
Copy code
{
  "first_name": "Updated",
  "last_name": "User",
  "email": "updated.user@example.com",
  "age": 30
}
Delete User:

Method: DELETE
URL: http://localhost:8000/users/<user_id>/
Stopping the Application
To stop the Docker containers, use the following command:

bash
Copy code
docker-compose down
Contributing
Feel free to contribute to this project by submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
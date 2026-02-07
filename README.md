# FastAPI MySQL Database Application

A production-ready FastAPI application for accessing and managing MySQL database data. This application provides RESTful APIs for CRUD operations on User and Post entities.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **MySQL Database**: Integration with MySQL using SQLAlchemy ORM
- **RESTful API**: Complete CRUD operations for Users and Posts
- **Data Validation**: Request/response validation using Pydantic
- **Auto-generated Documentation**: Interactive API docs with Swagger UI and ReDoc
- **Environment Configuration**: Easy configuration using environment variables
- **CORS Support**: Cross-Origin Resource Sharing enabled

## Project Structure

```
fastapi-mysql-db/
├── main.py           # FastAPI application entry point
├── database.py       # Database configuration and connection
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic schemas for validation
├── crud.py           # CRUD operations
├── routes.py         # API route definitions
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment variables
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Requirements

- Python 3.8+
- MySQL 5.7+ or MySQL 8.0+
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sachinashoka/fastapi-mysql-db.git
   cd fastapi-mysql-db
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   ```sql
   CREATE DATABASE fastapi_db;
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

## Configuration

Edit the `.env` file with your MySQL database credentials:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fastapi_db

APP_NAME=FastAPI MySQL Application
APP_VERSION=1.0.0
DEBUG=True
```

**Security Note**: The CORS configuration in `main.py` is set to allow specific origins. Update the `allow_origins` list with your actual frontend URLs in production.

## Running the Application

Start the FastAPI server:

```bash
# Using Python directly
python main.py

# Or using uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at:
- API: http://localhost:8000
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

### Root Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint

### User Endpoints

- `POST /users/` - Create a new user
- `GET /users/` - Get list of users (with pagination)
- `GET /users/{user_id}` - Get a specific user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

### Post Endpoints

- `POST /posts/` - Create a new post
- `GET /posts/` - Get list of posts (with pagination and optional author filter)
- `GET /posts/{post_id}` - Get a specific post by ID
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post

## API Usage Examples

### Create a User

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "full_name": "John Doe"
  }'
```

### Get All Users

```bash
curl -X GET "http://localhost:8000/users/"
```

### Create a Post

```bash
curl -X POST "http://localhost:8000/posts/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first post",
    "author": "johndoe"
  }'
```

### Get All Posts

```bash
curl -X GET "http://localhost:8000/posts/"
```

### Filter Posts by Author

```bash
curl -X GET "http://localhost:8000/posts/?author=johndoe"
```

## Database Models

### User Model

- `id`: Integer (Primary Key)
- `username`: String (Unique, Max 50 chars)
- `email`: String (Unique, Max 100 chars)
- `full_name`: String (Optional, Max 100 chars)
- `created_at`: DateTime (Auto-generated)
- `updated_at`: DateTime (Auto-updated)

### Post Model

- `id`: Integer (Primary Key)
- `title`: String (Max 200 chars)
- `content`: Text
- `author`: String (Max 50 chars) - Note: Uses username string for simplicity
- `created_at`: DateTime (Auto-generated)
- `updated_at`: DateTime (Auto-updated)

**Note**: The current implementation uses a simple string reference for the post author field for simplicity. In a production environment, you may want to add a foreign key relationship between Post and User models.

## Development

### Testing the Application

You can test the API using:
- Swagger UI at http://localhost:8000/docs
- cURL commands (see examples above)
- Postman or any API testing tool

### Database Migrations

The application automatically creates database tables on startup. For more advanced migration management, consider using Alembic.

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **PyMySQL**: Pure Python MySQL client
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server implementation
- **python-dotenv**: Environment variable management

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or contributions, please open an issue on GitHub.
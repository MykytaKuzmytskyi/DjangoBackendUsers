# User Management and Transactions API

API for managing users and their transactions, with JWT-based authentication.

### Installing using GitHub

Install PostgresSQL and create db

1. Clone the source code:

```bash
git clone https://github.com/MykytaKuzmytskyi/DjangoBackendUsers.git
cd DjangoBackendUsers
```
2. Install PostgresSQL and create DB.
3. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

4. `.env_sample` 
This is a sample .env file for use in local development.
Duplicate this file as .env in the root of the project
and update the environment variables to match your
desired config. You can use [djecrety.ir](https://djecrety.ir/)

5. Use the command to configure the database and tables:

```bash
python manage.py migrate
```

6. Start the app:

```bash
python manage.py runserver
```

### Run with docker
Docker should be installed

```commandline
docker-compose build
docker-compose up
```

### Getting access
- You can use following superuser:
  - username: `admin`
  - password: `AzNvbA8583`

- get access token via /api/token/

## Features
- JWT authenticated
- Admin panel /admin/
- Managing users and transaction


In the `.env` file, configure the following variables:

- `SECRET_KEY` — Django’s secret key.
- `DEBUG` — Set to `True` for development, `False` for production.

Additionally, for PostgreSQL configuration, include the following variables:

- `POSTGRES_DB` — The name of the PostgreSQL database to use.
- `POSTGRES_USER` — The username for connecting to the PostgreSQL database.
- `POSTGRES_PASSWORD` — The password for the PostgreSQL user.
- `POSTGRES_HOST` — The hostname or IP address of the PostgreSQL server.
- `POSTGRES_PORT` — The port on which PostgreSQL is running (default is `5432`).

Here is a sample configuration:

```env
SECRET_KEY=django-insecure-oowtr9^9_37e*g_r%3(%f@1relxu^&o27v&^qdixgn%ud8pl-s
DEBUG=True

# PostgreSQL configuration
POSTGRES_DB=users
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

You can access the API documentation and Swagger UI using the following links:

- **API Schema**: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/) - This endpoint provides the OpenAPI schema for your API.
- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) - This user-friendly interface allows you to interact with your API endpoints.


#### User Management Endpoints

- `POST /api/token/` — Obtain JWT token.
- `POST /api/token/refresh/` — Refresh JWT token.
- `POST /api/add_user/` — Create a new user (admin only).
- `GET /api/get_user/{user_id}/` — Retrieve user details by ID.
- `GET /api/get_all_users/` — Get a list of all users (admin only).

#### Transaction Management Endpoints

- `POST /api/add_transaction/` — Add a new transaction.

#### Statistics Endpoint

- `GET /api/statistic/` — Retrieve statistics on users and transactions.
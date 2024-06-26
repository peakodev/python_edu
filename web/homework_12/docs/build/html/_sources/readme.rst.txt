Homework 12
===========

Description
-----------

The project is structured as follows:

-  ``requirements.txt``: This file lists the Python dependencies that
   need to be installed
-  ``migrations/``: alembic migrations
-  ``src/``: fastapi project folder
-  ``src/conf/config.py``: class with ability to get .env variables
   using pydantic_settings
-  ``src/database/``: folder with db connections and models
-  ``src/repository/``: folder with repositories scripts for users and
   contacts
-  ``src/routes/``: folder with routes for auth and contacts
-  ``src/schemas/``: folder with pydentic schemas
-  ``src/middleware/``: folder with middlewares
-  ``src/service/auth.py``: auth service with ability to hash password
   and JWT methods like access and refresh tokens
-  ``main.py``: fastapi entrypoint

Prepare env
-----------

Install libs
~~~~~~~~~~~~

.. code:: bash

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Running the postgres in Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run docker compose

.. code:: bash

   docker-compose up -d

Run migrations:

.. code:: bash

   alembic upgrade head

Run server for testing

.. code:: bash

   uvicorn main:app --host localhost --port 8008 --reload

.. Contacts API documentation master file, created by
   sphinx-quickstart on Sun Jun  9 12:56:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Contacts API's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Contacts API documentation
==========================

Contacts API provides a structured way to store and retrieve contact information.
It is designed with a RESTful architecture, making it easy to integrate with various platforms and services. 
The API is divided into several modules, including a main module and two repository modules for contacts and users.

The main module handles the core functionalities of the API, while the src.repository.contacts module manages the contact information, 
including operations like adding, updating, and deleting contacts. The src.repository.users module, 
on the other hand, manages user information and authentication, 
ensuring that only authorized users can access the contact data.

Overall, this Contacts API is a comprehensive solution for managing contact information in a secure and efficient manner.


The project is structured as follows:
=====================================

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


How to prepare the environment
==============================

1. Clone the repository
   .. code-block:: bash

      git clone git@github.com:peakodev/python_edu.git
      cd python_edu/web/homework_12

2. Create a virtual environment
   .. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate

3. Install the dependencies
   .. code-block:: bash

      pip install -r requirements.txt

4. Create a .env file with the variables from .env.default
   .. code-block:: bash

      cp .env.default .env

5. Run docker-compose up -d
   .. code-block:: bash

      docker-compose up -d

6. Run alembic upgrade head
   .. code-block:: bash

      alembic upgrade head

7. Run the project with uvicorn main:app --reload
   .. code-block:: bash

      uvicorn main:app --host localhost --port 8008 --reload


REST API main
===================
.. automodule:: main
  :members:
  :undoc-members:
  :show-inheritance:


REST API repository Contacts
============================
.. automodule:: src.repository.contacts
  :members:
  :undoc-members:
  :show-inheritance:


REST API repository Users
=========================
.. automodule:: src.repository.users
  :members:
  :undoc-members:
  :show-inheritance:


REST API routes Contacts
=========================
.. automodule:: src.routes.contacts
  :members:
  :undoc-members:
  :show-inheritance:


REST API routes Auth
=========================
.. automodule:: src.routes.users
  :members:
  :undoc-members:
  :show-inheritance:


REST API routes Auth
=========================
.. automodule:: src.routes.auth
  :members:
  :undoc-members:
  :show-inheritance:


REST API service Email
=========================
.. automodule:: src.services.email
  :members:
  :undoc-members:
  :show-inheritance:


REST API service Auth
=========================
.. automodule:: src.services.auth
  :noindex:
.. autofunction:: src.services.auth.Auth.verify_password
.. autofunction:: src.services.auth.Auth.get_password_hash
.. autofunction:: src.services.auth.Auth.create_access_token
.. autofunction:: src.services.auth.Auth.create_refresh_token
.. autofunction:: src.services.auth.Auth.create_email_token
.. autofunction:: src.services.auth.Auth.decode_refresh_token
.. autofunction:: src.services.auth.Auth.get_current_user
.. autofunction:: src.services.auth.Auth.get_email_from_token


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

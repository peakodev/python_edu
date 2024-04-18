# Homework 7

## Description

Work with database Postgres

The project is structured as follows:

- `alembic/versions/`: migrations folder using alembic
- `app/db.py`: connect to postgres instance, get session and get Base for models
- `app/models.py`: Student, Group, Teacher, Subject, Grade models using sqlalchemy
- `app/repository.py`: 12 sql queries from homework 7. For tunning this queries please use select_data.py
- `app/exceptions.py`: useful exceptions for project
- `app/factory.py`: factory classes for CRUD manipulations (used in crud.py)
- `seeds/seed.py`: populate DB with fake data using Faker
- `select_data.py`: the script that give ability to query 12 selects from homework
- `crud.py`: the script that give ability to create/read/update/delete and list models using argparse CLI
- `requirements.txt`: This file lists the Python dependencies that need to be installed
- `schema.sql`: SQL schema

## Running the postgres in Docker container

Run postgres in container

```bash
docker pull postgres
```

```bash
docker run --name pg_homework7 -e POSTGRES_PASSWORD=mysecretpassword -p 5552:5432 -d postgres
```

## Prepare env and data

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run migration using alembic

```bash
alembic upgrade head
```

Run seed/seed.py for generate fake data

```bash
python seed/seed.py
```

# Select Data Script (12 queries)

This script allows you to execute SQL SELECT queries on a database.

## Usage

The script is run from the command line with the following syntax:

```bash
python select_data.py QUERY_NUMBER [PARAMETERS...]
```

__**Where**__:

 - **QUERY_NUMBER** is the number of the query to execute. It should be an integer between 1 and 12.
 - **PARAMETERS** are the parameters for the query. The number and type of parameters depend on the query.

 If you run the script without any arguments, it will prompt you to enter the query number and parameters interactively.

 ## Examples

 To execute query number 3 with "John Doe" as a parameter:

```bash
python select_data.py 3 "John Doe"
```

To execute query number 5 with "Math" and "Grade 10" as parameters:

```bash
python select_data.py 5 "Math" "Grade 10"
```

To enter the query number and parameters interactively:

```bash
python select_data.py
```

Remember to replace these examples with your actual usage. You should also add error checking and handling as needed.

# CRUD Operations Script

This script allows you to perform CRUD (Create, Read, Update, Delete) operations on different models in a database.

## Usage

The script is run from the command line with the following syntax:

```bash
python crud.py -a ACTION -m MODEL [--name NAME] [--id ID] [--grade GRADE] [--teacher_id TEACHER_ID] [--group_id GROUP_ID] [--subject_id SUBJECT_ID] [--student_id STUDENT_ID]
```

__**Where**__:

- **ACTION** is the CRUD operation to perform. It can be one of the following: create, list, update, delete, read.
- **MODEL** is the model to perform the operation on. It can be one of the following: Teacher, Group, Student, Subject, Grade.
- **NAME** is the name for create and update actions.
- **ID** is the id for update and remove actions.
- **GRADE** is the grade for create and update Grade.
- **TEACHER_ID** is the teacher_id for create and update Subject.
- **GROUP_ID** is the group_id for create and update Student.
- **SUBJECT_ID** is the subject_id for create and update Grade.
- **STUDENT_ID** is the student_id for create and update Grade.

## Examples

To create a new student:

```bash
python crud.py -a create -m Student --name "John Doe" --group_id 1
```

 To update a teacher:

 ```bash
python crud.py -a update -m Teacher --id 1 --name "Jane Doe"
```

To delete a grade:

```bash
python crud.py -a delete -m Grade --id 1
```

To list all subjects:

```bash
python crud.py -a list -m Subject
```

To read a specific group:

```bash
python crud.py -a read -m Group --id 1
```

To create grade for specific student and subject:

```bash
py crud.py -a create -m Grade --grade 5 --student_id 51 --subject_id 2
```

Remember to replace these examples with your actual usage. You should also add error checking and handling as needed.
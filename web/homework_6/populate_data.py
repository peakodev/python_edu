from connection import create_connection, dsn_str
from faker import Faker
import random

fake = Faker()


def insert_data():
    with create_connection(dsn_str) as conn:
        with conn.cursor() as cur:
            data_faker(cur)

        conn.commit()


def data_faker(cur):
    # Insert groups
    for _ in range(3):
        cur.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))

    # Get group ids
    cur.execute("SELECT id FROM groups")
    group_ids = [row[0] for row in cur.fetchall()]

    # Insert students
    for _ in range(50):
        cur.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)",
                    (fake.name(), random.choice(group_ids)))

    # Insert teachers
    for _ in range(5):
        cur.execute("INSERT INTO teachers (name) VALUES (%s)", (fake.name(),))

    # Get teacher ids
    cur.execute("SELECT id FROM teachers")
    teacher_ids = [row[0] for row in cur.fetchall()]

    # Insert subjects
    for _ in range(8):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)",
                    (fake.word(), random.choice(teacher_ids)))

    # Get student and subject ids
    cur.execute("SELECT id FROM students")
    student_ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM subjects")
    subject_ids = [row[0] for row in cur.fetchall()]

    # Insert grades
    for student_id in student_ids:
        for subject_id in subject_ids:
            for _ in range(random.randint(0, 20)):
                cur.execute("INSERT INTO grades (student_id, subject_id, grade, received_at) VALUES (%s, %s, %s, %s)",
                            (student_id, subject_id, random.randint(1, 10), fake.date_time_this_year()))


if __name__ == '__main__':
    insert_data()

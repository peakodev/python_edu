import random

from faker import Faker

from app.db import session
from app.models import Group, Student, Teacher, Subject, Grade


def make_fake_data():
    # create groups
    for _ in range(3):
        group = Group(name=fake.word())
        session.add(group)

    session.commit()

    # create students
    for _ in range(50):
        group_id = random.choice(session.query(Group.id).all())[0]
        student = Student(name=fake.name(), group_id=group_id)
        session.add(student)

    session.commit()

    # create teachers
    for _ in range(5):
        teacher = Teacher(name=fake.name())
        session.add(teacher)

    session.commit()

    # create subjects
    for _ in range(8):
        teacher_id = random.choice(session.query(Teacher.id).all())[0]
        subject = Subject(name=fake.word(), teacher_id=teacher_id)
        session.add(subject)

    session.commit()

    # create grades
    for student in session.query(Student).all():
        for subject in session.query(Subject).all():
            for _ in range(random.randint(1, 20)):
                grade = Grade(grade=random.randint(1, 5),
                              student_id=student.id,
                              subject_id=subject.id,
                              received_at=fake.date_time_this_year())
                session.add(grade)

    session.commit()


if __name__ == "__main__":
    fake = Faker()
    make_fake_data()

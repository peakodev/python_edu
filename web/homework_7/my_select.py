from sqlalchemy import func, desc

from app.db import session
from app.models import Group, Student, Teacher, Subject, Grade


def select_1():
    """
    Find the top 5 students with the highest average grade across all subjects.
    """
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(
        Student
    ).join(
        Grade
    ).group_by(
        Student.name
    ).order_by(
        desc('average_grade')
    ).limit(5).all()


def select_2(subject_name: str):
    """
    Find the student with the highest average grade in the subject <subject_name>.
    """
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(
        Student
    ).join(
        Grade
    ).join(
        Subject
    ).filter(
        Subject.name == subject_name
    ).group_by(
        Student.name
    ).order_by(
        desc('average_grade')
    ).limit(1).first()


def select_3(subject_name: str):
    """
    Find the average grade for the subject <subject_name> across all students.
    """
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(
        Group
    ).join(
        Student
    ).join(
        Grade
    ).join(
        Subject
    ).filter(
        Subject.name == subject_name
    ).group_by(
        Student.name
    ).all()


def select_4():
    pass


def select_5():
    pass


def select_6():
    pass


def select_7():
    pass


def select_8():
    pass


def select_9():
    pass


def select_10():
    pass


def select_11():
    pass


def select_12():
    pass


print(select_2('never'))

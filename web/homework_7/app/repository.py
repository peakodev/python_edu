from sqlalchemy import func, desc, select, and_

from app.models import Group, Student, Teacher, Subject, Grade


def select_1(_):
    """
    Find the top 5 students with the highest average grade across all subjects.
    """
    return select(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(Student).join(Grade).group_by(
        Student.name
    ).order_by(
        desc('average_grade')
    ).limit(5)


def select_2(subject_name: str):
    """
    Find the student with the highest average grade in the subject <subject_name>.
    """
    return select(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(Student).join(Grade).join(Subject).filter(
        Subject.name == subject_name
    ).group_by(
        Student.name
    ).order_by(
        desc('average_grade')
    ).limit(1)


def select_3(subject_name: str):
    """
    Find the average grade for the subject <subject_name> across all students.
    """
    return select(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(Group).join(Student).join(Grade).join(Subject).filter(
        Subject.name == subject_name
    ).group_by(
        Student.name
    )


def select_4(_):
    """
    Find the average grade in the stream (across the entire grades table).
    """
    return select(
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(Grade).limit(1)


def select_5(teacher_name: str):
    """
    Find all subjects taught by the teacher <teacher_name>.
    """
    return select(
        Subject.name
    ).select_from(Subject).join(Teacher).where(Teacher.name.ilike(f'%{teacher_name}%'))


def select_6(group_name: str):
    """
    Find all students from group <group_name>.
    """
    return select(
        Student.name,
    ).select_from(Student).join(Group).filter(Group.name == group_name)


def select_7(group_name: str, subject_name: str):
    """
    Find all students from group <group_name> who have received a grade for the subject <subject_name>.
    """
    return select(
        Student.name,
        Grade.grade,
        func.date(Grade.received_at).label('received_at'),
    ).select_from(Student).join(Grade).join(Subject).join(Group).filter(
        Group.name == group_name
    ).filter(
        Subject.name == subject_name
    ).order_by(desc('received_at'))


def select_8(teacher_name: str):
    """
    Find the average grade that a specific teacher gives for their subjects.
    """
    return select(
        Teacher.name,
        func.round(func.avg(Grade.grade), 2).label("average_grade")
    ).select_from(Teacher).join(Subject).join(Grade).filter(
        Teacher.name.ilike(f'%{teacher_name}%')
    ).group_by(Teacher.name)


def select_9(student_name: str):
    """
    Find the list of courses a student attends.
    """
    return select(
        Subject.name
    ).select_from(Subject).outerjoin(Grade).outerjoin(Student).filter(
        Student.name.ilike(f'%{student_name}%')
    ).group_by(Subject.name)


def select_10(student_name: str, teacher_name: str):
    """
    List of courses that a specific student is taught by a specific teacher.
    """
    return select(
        Subject.name
    ).select_from(Subject).join(Grade).join(Student).join(Teacher).filter(
        Student.name.ilike(f'%{student_name}%')
    ).filter(
        Teacher.name.ilike(f'%{teacher_name}%')
    ).group_by(Subject.name)


def select_11(student_name: str, teacher_name: str):
    """
    Find the average grade of a specific student for a specific teacher.
    """
    return select(
        Student.name.label("student"),
        func.round(func.avg(Grade.grade), 2).label("average_grade"),
        Teacher.name.label("teacher"),
    ).select_from(Grade).join(Subject).join(Teacher).join(Student).filter(
        Student.name.ilike(f'%{student_name}%')
    ).filter(
        Teacher.name.ilike(f'%{teacher_name}%')
    ).group_by(Student.name, Teacher.name)


def select_12(group_name: str, subject_name: str):
    """
    The grades of students in a specific group for a specific subject at the last lesson.
    """
    subquery = select(
        func.max(func.date(Grade.received_at)).label('received_at')
    ).select_from(Grade).join(Student).join(Subject).where(
        and_(Group.name == group_name, Subject.name == subject_name)
    ).scalar_subquery()

    return select(
        Student.name.label("student"),
        Grade.grade,
        func.date(Grade.received_at).label('received_at')
    ).select_from(Student).join(Grade).join(Subject).join(Group).where(
        and_(Group.name == group_name, Subject.name == subject_name,
             func.date(Grade.received_at) == subquery)
    )


def get_select(number: int) -> tuple:
    functions = {
        1: (select_1, None),
        2: (select_2, ('subject',)),
        3: (select_3, ('subject',)),
        4: (select_4, None),
        5: (select_5, ('teacher',)),
        6: (select_6, ('group',)),
        7: (select_7, ('group', 'subject')),
        8: (select_8, ('teacher',)),
        9: (select_9, ('student',)),
        10: (select_10, ('student', 'teacher')),
        11: (select_11, ('student', 'teacher')),
        12: (select_12, ('group', 'subject')),
    }

    return functions.get(number, (None,))

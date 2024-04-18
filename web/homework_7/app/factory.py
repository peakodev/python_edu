from abc import ABC

from app.db import Base, session
from app.models import Student, Group, Teacher, Subject, Grade
from app.exceptions import ModelNotFound
from datetime import datetime


class ModelFactory(ABC):
    __model__ = None

    def accept(self, type: str) -> bool:
        return self.__model__.__name__ == type

    def create(self, name: str) -> Base:
        model = self.__model__(name=name)
        session.add(model)
        session.commit()
        return model

    def update(self, id: int, name: str) -> Base:
        model = self.read(id)
        model.name = name
        session.commit()
        return model

    def read(self, id: int) -> Base:
        model = session.get(self.__model__, id)
        if not model:
            raise ModelNotFound(f'The {self.__model__.__name__} with id {id} does not exist.')
        return model

    def delete(self, id: int) -> None:
        model = self.read(id)
        session.delete(model)
        session.commit()

    def list(self) -> list[Base]:
        return session.query(self.__model__).all()


class StudentFactory(ModelFactory):
    __model__ = Student

    def create(self, name: str, group_id: int) -> Base:
        group = GroupFactory().read(group_id)
        model = self.__model__(name=name, group_id=group.id)
        session.add(model)
        session.commit()
        return model

    def update(self, id: int, name: str, group_id: int) -> Base:
        model = self.read(id)
        group = GroupFactory().read(group_id)
        model.name = name
        model.group_id = group.id
        session.commit()
        return model


class GroupFactory(ModelFactory):
    __model__ = Group


class TeacherFactory(ModelFactory):
    __model__ = Teacher


class SubjectFactory(ModelFactory):
    __model__ = Subject

    def create(self, name: str, teacher_id: int) -> Base:
        teacher = TeacherFactory().read(teacher_id)
        model = self.__model__(name=name, teacher_id=teacher.id)
        session.add(model)
        session.commit()
        return model

    def update(self, id: int, name: str, teacher_id: int) -> Base:
        model = self.read(id)
        teacher = TeacherFactory().read(teacher_id)
        model.name = name
        model.teacher_id = teacher.id
        session.commit()
        return model


class GradeFactory(ModelFactory):
    __model__ = Grade

    def create(self, grade: int, student_id: int, subject_id: int) -> Base:
        student = StudentFactory().read(student_id)
        subject = SubjectFactory().read(subject_id)
        model = self.__model__(grade=grade, student_id=student.id, subject_id=subject.id)
        model.received_at = datetime.today()
        session.add(model)
        session.commit()
        return model

    def update(self, id: int, grade: int, student_id: int, subject_id: int) -> Base:
        model = self.read(id)
        student = StudentFactory().read(student_id)
        subject = SubjectFactory().read(subject_id)
        model.grade = grade
        model.student_id = student.id
        model.subject_id = subject.id
        session.commit()
        return model

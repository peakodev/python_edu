from abc import ABC
from argparse import ArgumentParser

from app.db import Base, session
from app.models import Student, Group, Teacher, Subject
from app.exceptions import ModelNotFound, FactoryNotFound, MethodNotFound, BaseException


def get_parser() -> ArgumentParser:
    p = ArgumentParser(description='Perform CRUD operations on the database.')
    p.add_argument('-a', '--action',
                   choices=['create', 'list', 'update', 'delete', 'read'],
                   required=True,
                   help='The CRUD operation to perform.')
    p.add_argument('-m', '--model',
                   choices=['Teacher', 'Group', 'Student', 'Subject'],
                   required=True,
                   help='The model to perform the operation on.')
    p.add_argument('--name', help='The name for create and update actions.')
    p.add_argument('--id', type=int, help='The id for update and remove actions.')
    p.add_argument('--teacher_id', type=int, help='The teacher_id for create and update Subject.')
    p.add_argument('--group_id', type=int, help='The group_id for create and update Student.')
    return p


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


class GroupFactory(ModelFactory):
    __model__ = Group


class TeacherFactory(ModelFactory):
    __model__ = Teacher


class SubjectFactory(ModelFactory):
    __model__ = Subject


class FactoryProducer:
    __factories = [
        StudentFactory(),
        GroupFactory(),
        TeacherFactory(),
        SubjectFactory()
    ]

    def __init__(self, type: str) -> None:
        self.factory = self.get_factory(type)
        if not self.factory:
            raise FactoryNotFound(f'The factory for {type} does not exist.')

    def get_factory(self, type: str) -> ModelFactory:
        return next((factory for factory in self.__factories if factory.accept(type)), None)

    def method(self, action: str):
        self.action = action
        self.method = getattr(self.factory, action, None)
        if not self.method or not callable(self.method):
            raise MethodNotFound(f'The method {action} does not exist for {self.factory.__model__}.')
        return self

    def execute(self, name: str = None, id: int = None):
        if self.action == 'create':
            return self.method(name)
        elif self.action == 'update':
            return self.method(id, name)
        elif self.action in ['read', 'delete']:
            return self.method(id)
        elif self.action == 'list':
            return self.method()


def main():
    args = get_parser().parse_args()
    try:
        producer = FactoryProducer(args.model)
        result = producer.method(args.action).execute(args.name, args.id)
        print(result)
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    main()

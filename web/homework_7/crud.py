from argparse import ArgumentParser
from pprint import pprint

from sqlalchemy import inspect

from app.exceptions import FactoryNotFound, MethodNotFound, BaseException
from app.factory import StudentFactory, GroupFactory, TeacherFactory, SubjectFactory, GradeFactory, ModelFactory


def get_parser() -> ArgumentParser:
    p = ArgumentParser(description='Perform CRUD operations on the database.')
    p.add_argument('-a', '--action',
                   choices=['create', 'list', 'update', 'delete', 'read'],
                   required=True,
                   help='The CRUD operation to perform.')
    p.add_argument('-m', '--model',
                   choices=['Teacher', 'Group', 'Student', 'Subject', 'Grade'],
                   required=True,
                   help='The model to perform the operation on.')
    p.add_argument('--name', help='The name for create and update actions.')
    p.add_argument('--id', type=int, help='The id for update and remove actions.')
    p.add_argument('--grade', type=int, help='The grade for create and update Grade.')
    p.add_argument('--teacher_id', type=int, help='The teacher_id for create and update Subject.')
    p.add_argument('--group_id', type=int, help='The group_id for create and update Student.')
    p.add_argument('--subject_id', type=int, help='The subject_id for create and update Grade.')
    p.add_argument('--student_id', type=int, help='The student_id for create and update Grade.')
    return p


class FactoryProducer:
    __factories = [
        StudentFactory(),
        GroupFactory(),
        TeacherFactory(),
        SubjectFactory(),
        GradeFactory()
    ]

    def __init__(self, type: str) -> None:
        self.factory = self.get_factory(type)
        if not self.factory:
            raise FactoryNotFound(f'The factory for {type} does not exist.')

    def get_factory(self, type: str) -> ModelFactory:
        return next((factory for factory in self.__factories if factory.accept(type)), None)

    def get_method(self, action: str):
        self.action = action
        self.method = getattr(self.factory, action, None)
        if not self.method or not callable(self.method):
            raise MethodNotFound(f'The method {action} does not exist for {self.factory.__model__}.')
        return self

    def get_args(self, arguments):
        """
        Get the arguments for the method from the arguments passed to the script.
        """
        model_args_iter = inspect(self.factory.__model__).mapper.column_attrs
        self.args = tuple({arg.key: getattr(arguments, arg.key)} for arg in model_args_iter
                          if arg.key in vars(arguments) and getattr(arguments, arg.key) is not None)
        return self

    def execute(self):
        args_dict = {k: v for d in self.args for k, v in d.items()}
        return self.method(**args_dict)


def main():
    args = get_parser().parse_args()
    try:
        producer = FactoryProducer(args.model)
        result = producer.get_method(args.action).get_args(args).execute()
        pprint(result)
    except BaseException as e:
        pprint(e)


if __name__ == '__main__':
    main()

from setuptools import setup, find_namespace_packages

setup(
    name='phone_book',
    version='0.0.1',
    entry_points={
        'console_scripts': []
    },
    description='Phone book',
    author='Nazar Salo',
    author_email='peakodev@gmail.com',
    packages=find_namespace_packages(),
    install_requires=[],
    url='https://github.com/peakodev/python_edu/tree/main/homework_12/phone_book'
)
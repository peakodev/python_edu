from setuptools import setup, find_namespace_packages

setup(
    name='phone_book_bot',
    version='0.0.1',
    entry_points={
        'console_scripts': ['phonebot = phone_book_bot.bot:bot_start']
    },
    description='Phone book Bot',
    author='Nazar Salo',
    author_email='peakodev@gmail.com',
    packages=find_namespace_packages(),
    install_requires=['phone_book>=0.0.1', 'faker'],
)
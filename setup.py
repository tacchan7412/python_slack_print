from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python_slack_print',
    version='1.0.5',
    description='Python print for stdout and slack',
    long_description=long_description,
    url='https://github.com/tacchan7412/python_slack_print',
    author='Tatsuki Koga',
    author_email='tacchan.04@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['slacker']
)

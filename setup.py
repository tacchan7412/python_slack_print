from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python_slack_print',
    version='1.0.0',
    description='Python print for stdout and slack',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tacchan7412/python_slack_print',
    author='Tatsuki Koga',
    license='MIT',
    packages=find_packages('slack_print'),
    install_requires=['slacker']
)

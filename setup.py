import os
from setuptools import find_packages
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='gq',
    version=__import__('gq').__version__,
    description='a query-like selector for maf data',
    long_description=readme,
    author='Yoshihiro Nagano',
    author_email='y.nagano.92@gmail.com',
    licence='MIT License',
    url='http://github.com/ganow/gq/',
    install_requires = open('requirements.txt').read().splitlines(),
    packages=['gq'],
    classifiers = [
        'Programming Language :: Python :: 2.7.7',,
        'License :: OSI Approved :: MIT License'
    ]
)
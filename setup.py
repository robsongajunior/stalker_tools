# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='stalker-tools',
    version='0.0.1',
	description='The propose of projetct is to facilitate some non-tech people to follow a relatory of state informations.'
    license='MIT',
    url='https://github.com/robsongajunior/stalker-tools',
    author='Robson Gomes de Araújo Júnior',
    author_email='robson.junior@gmail.com',
    maintainer='Robson Júnior',
    author_email='robson.junior@gmail.com',
    keywords=[
        'dns resolution',
        'headers information'
    ],
    install_requires=open('requirements.txt').read(),
    tests_require=open('requirements-test.txt').read(),
    dependency_links=[],
    packages=find_packages(),
    data_files = [],
)

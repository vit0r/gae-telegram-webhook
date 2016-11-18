# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='tg_send',
    version=0.1,
    license='BSD',
    url='https://www.github.com/vit0r/tg_send',
    author='Vitor Nascimento Araújo',
    author_email='',
    description='Simple telegram webhook send message',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    install_requires=['httplib2==0.9.2', 'PyYAML==3.11', 'nose==1.3.7']
)

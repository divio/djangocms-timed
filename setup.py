#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from djangocms_timed import __version__

REQUIREMENTS = []

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='djangocms-timed',
    version=__version__,
    description='Timed addon for django CMS',
    long_description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/djangocms-timed',
    packages=find_packages(),
    license='BSD License',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.settings.run',
)

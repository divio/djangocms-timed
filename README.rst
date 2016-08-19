================
django CMS Timed
================


|pypi| |build| |coverage|

**django CMS Timed** is plugins for `django CMS <http://django-cms.org>`_
that allow you to display plugins content within a defined period of time.

This addon is compatible with `Aldryn <http://aldryn.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/djangocms-timed/>`_
for easy installation.


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.


Documentation
=============


See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-timed/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.6 or higher


Installation
------------

For a manual install:

* run ``pip install djangocms-timed``
* add ``djangocms_timed`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_timed``


Configuration
-------------

Note that the provided templates are very minimal by design. You are encouraged
to adapt and override them to your project's requirements.


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/djangocms-timed.svg
    :target: http://badge.fury.io/py/djangocms-timed
.. |build| image:: https://travis-ci.org/divio/djangocms-timed.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-timed
.. |coverage| image:: https://codecov.io/gh/divio/djangocms-timed/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-timed
Aldryn Timed Add-on
===================

It allows you to display plugins content within a defined period of time.

Installation
============

Aldryn Platrofm Users
---------------------

Choose a site you want to install the add-on to from the dashboard. Then go to ``Apps -> Install app`` and click ``Install`` next to ``Timed`` app.

Redeploy the site.

Manuall Installation
--------------------

Run ``pip install aldryn-timed``.

Add below apps to ``INSTALLED_APPS``:

    INSTALLED_APPS = [
        …
        'aldryn_timed',
        …
    ]


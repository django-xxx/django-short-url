================
django-short-url
================

Django WeChat Short URL

Installation
============

::

    pip install django-short-url


Usage
=====

::

    from django_short_url.views import get_surl

    def xxx(request):
        surl = get_surl(lurl)


Urls.py
=======

::

    urlpatterns = [
        url(r'^s/', include('django_short_url.urls', namespace='django_short_url')),
    ]


or::

    urlpatterns = [
        url(r'^(?P<surl>\w+)', surl_views.short_url_redirect, name='short_url_redirect'),
    ]


Settings.py
===========

::

    INSTALLED_APPS = (
        ...
        'django_short_url',
        ...
    )

    # Redirect url when short url not exists
    DJANGO_SHORT_URL_REDIRECT_URL = ''


# -*- coding: utf-8 -*-


from django_six import re_path

from django_short_url import views as surl_views


app_name = 'django_short_url'


urlpatterns = [
    re_path(r'^(?P<surl>\w+)', surl_views.short_url_redirect, name='short_url_redirect'),
]

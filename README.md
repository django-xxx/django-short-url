# django-short-url
Django Short URL

## Installation
```shell
pip install django-short-url
```

## Usage
```python
from django_short_url.views import get_surl

def xxx(request):
    surl = get_surl(lurl)
```

## Urls.py
```python
urlpatterns = [
    url(r'^s/', include('django_short_url.urls', namespace='django_short_url')),
]
```
or
```python
from django.urls import re_path
from django_short_url import views as surl_views

urlpatterns = [
    re_path(r'^(?P<surl>\w+)', surl_views.short_url_redirect, name='short_url_redirect'),
]
```

## Settings.py
```python
INSTALLED_APPS = (
    ...
    'django_short_url',
    ...
)

# Redirect url when short url not exists
DJANGO_SHORT_URL_REDIRECT_URL = ''
```

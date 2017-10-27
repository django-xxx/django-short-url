# -*- coding: utf-8 -*-

import shortuuid
from CodeConvert import CodeConvert as cc
from django.conf import settings
from django.shortcuts import redirect, render
from django_short_url.models import ShortURL
from furl import furl


def short_url_redirect(request, surl):
    """
    >> Chrome 请求
    ?nickname=姜戈

    >> Django 获取
    u'?nickname=%E5%A7%9C%E6%88%88'

    >> furl(lurl).add(furl(request.get_raw_uri()).query.params).url
    ?nickname=%C3%A5%C2%A7%C2%9C%C3%A6%C2%88%C2%88

    >> furl(lurl).add(furl(cc.Convert2Utf8(request.get_raw_uri())).query.params).url
    ?nickname=%E5%A7%9C%E6%88%88
    """
    try:
        lurl = ShortURL.objects.get(surl=surl).lurl
    except ShortURL.DoesNotExist:
        lurl = None

    # Short URL Not Exists
    if not lurl:
        redirect_url = ''

        if hasattr(settings, 'DJANGO_SHORT_URL_REDIRECT_URL'):
            redirect_url = settings.DJANGO_SHORT_URL_REDIRECT_URL

        if hasattr(settings, 'DJANGO_SHORT_URL_FUNC') and hasattr(settings.DJANGO_SHORT_URL_FUNC, '__call__'):
            redirect_url = settings.DJANGO_SHORT_URL_FUNC(request)

        if not redirect_url:
            return render(request, 'django_short_url/errmsg.html', {'title': 'Error', 'errmsg': 'Short URL not Exists'})

        return redirect(redirect_url)

    return redirect(furl(lurl).add(furl(cc.Convert2Utf8(request.get_raw_uri())).query.params).url)


def get_surl(lurl):
    return ShortURL.objects.get_or_create(lurl=lurl, defaults={
        'surl': shortuuid.uuid()
    })[0].fsurl

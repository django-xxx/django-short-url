# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ShortURL(models.Model):
    surl = models.CharField(_(u'surl'), max_length=32, blank=True, null=True, help_text=u'短链', db_index=True, unique=True)
    lurl = models.CharField(_(u'lurl'), max_length=255, blank=True, null=True, help_text=u'长链', db_index=True, unique=True)

    status = models.BooleanField(_(u'status'), default=True, help_text=u'是否显示', db_index=True)

    created_at = models.DateTimeField(_(u'created_at'), auto_now_add=True, editable=True, help_text=_(u'创建时间'))
    updated_at = models.DateTimeField(_(u'updated_at'), auto_now=True, editable=True, help_text=_(u'更新时间'))

    class Meta:
        verbose_name = _(u'shorturl')
        verbose_name_plural = _(u'shorturl')

    def __unicode__(self):
        return unicode(self.pk)

    @property
    def fdomain(self):
        if hasattr(settings, 'DJANGO_SHORT_URL_DOMAIN'):
            return settings.DJANGO_SHORT_URL_DOMAIN
        elif hasattr(settings, 'DOMAIN'):
            return settings.DOMAIN
        return ''

    @property
    def fsurl(self):
        return u'{}/s/{}'.format(self.fdomain, self.surl)

    @property
    def data(self):
        return {
            'lurl': self.lurl,
            'surl': self.fsurl,
        }

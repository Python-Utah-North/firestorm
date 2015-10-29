# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.http import urlquote
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME


def login_url_with_redirect(request):
    path = urlquote(request.get_full_path())
    url = '%s?%s=%s' % (settings.LOGIN_URL, REDIRECT_FIELD_NAME, path)
    return {'login_url': url}

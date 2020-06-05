# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.module_loading import import_string as _load
from django.core.exceptions import DisallowedHost
from django.http import HttpResponseForbidden
from .models import ActivityLog
from . import conf


class ActivityLogMiddleware:
    def process_request(self, request):
        request.saved_body = request.body
        if conf.LAST_ACTIVITY and request.user.is_authenticated():
            getattr(request.user, 'update_last_activity', lambda: 1)()

    def process_response(self, request, response):
        try:
            self._write_log(request, response, getattr(request, 'saved_body', ''))
        except DisallowedHost:
            return HttpResponseForbidden()
        return response

    def _write_log(self, request, response, body):
        miss_log = [
            not(conf.ANONIMOUS or request.user.is_authenticated()),
            request.method not in conf.METHODS,
            any(url in request.path for url in conf.EXCLUDE_URLS)
        ]

        if conf.STATUSES:
            miss_log.append(response.status_code not in conf.STATUSES)

        if conf.EXCLUDE_STATUSES:
            miss_log.append(response.status_code in conf.EXCLUDE_STATUSES)

        if any(miss_log):
            return

        if getattr(request, 'user', None) and request.user.is_authenticated():
            user, user_id = request.user.get_username(), request.user.pk
        elif getattr(request, 'session', None):
            user, user_id = 'anon_{}'.format(request.session.session_key), 0
        else:
            return

        ActivityLog.objects.create(
            user_id=user_id,
            user=user,
            user_location=user_location,
            activity_period = activity_period
        )

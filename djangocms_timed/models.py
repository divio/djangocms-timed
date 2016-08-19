from __future__ import unicode_literals

from django import core
from django.db import models
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from cms.models.pluginmodel import CMSPlugin


class TimedContentPlugin(CMSPlugin):
    timed_start = models.DateTimeField(
        _('Visible since'),
        null=True, blank=True,
    )
    timed_end = models.DateTimeField(
        _('Visible until'),
        null=True, blank=True
    )

    @property
    def is_visible(self):
        start = self.timed_start
        end = self.timed_end
        now = timezone.now()

        if start and now < start:
            # start is in the future
            return False

        if end and now > end:
            # end is in the past
            return False

        return True

    def get_display(self):
        def pretty_date(dt):
            if not dt:
                return
            return dt.strftime('%d %b %Y %H:%M')

        visible = self.is_visible
        start = self.timed_start
        end = self.timed_end

        if start and end:
            if start > end:
                message = _('Always hidden')
            elif visible:
                message = _('Visible since {start} until {end}')
            elif end < timezone.now():
                message = _('Hidden since {end}')
            else:
                message = _('Hidden until {start}')

        elif start and not end:
            if visible:
                message = _('Visible since {start}')
            else:
                message = _('Hidden until {start}')

        elif not start and end:
            if visible:
                message = _('Visible until {end}')
            else:
                message = _('Hidden since {end}')

        else:
            message = _('Always visible')

        return message.format(
            start=pretty_date(start),
            end=pretty_date(end),
        )

    def get_short_description(self):
        instance = self.get_plugin_instance()[0]
        if instance is not None:
            return force_text(self.get_display())
        return _('<Empty>')  # pragma: no cover

    def clean(self):
        start = self.timed_start
        end = self.timed_end

        if start and end and start > end:
            raise core.exceptions.ValidationError(_(
                'The start datetime has to be earlier than the end datetime.'
            ))

        return super(TimedContentPlugin, self).clean()

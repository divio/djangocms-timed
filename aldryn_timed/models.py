from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from cms.models.pluginmodel import CMSPlugin


class TimedPlugin(CMSPlugin):

    publication_start = models.DateTimeField(_('Published Since'),
                                             default=now)
    publication_end = models.DateTimeField(_('Published Until'),
                                           null=True, blank=True)

    @property
    def is_published(self):
        start = self.publication_start
        end = (self.publication_end
               if self.publication_end else None)
        if start <= now() and (not end or end >= now()):
            return True
        return False

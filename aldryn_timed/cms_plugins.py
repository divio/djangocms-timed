# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TimedPlugin


class TimedPlugin(CMSPluginBase):

    module = _('Timed')
    render_template = 'aldryn_timed/timed.html'
    name = _('Timed container')
    model = TimedPlugin
    allow_children = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(TimedPlugin)

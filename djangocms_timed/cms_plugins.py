# -*- coding: utf-8 -*-
from django.utils.encoding import force_str
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class TimedContent(CMSPluginBase):
    name = _('Timed content')
    model = models.TimedContentPlugin
    render_template = 'djangocms_timed/timed.html'
    allow_children = True
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TimedContent, self).render(context, instance, placeholder)
        visible = instance.is_visible
        child_plugins = instance.child_plugin_instances or []
        context.update({
            'child_plugins': child_plugins,
            'visible': visible,
            'visible_in_edit': (
                not visible and
                child_plugins and
                context['request'].session.get('cms_edit')
            ),
        })
        return context

    def __repr__(self):
        return force_str(super(TimedContent, self).__repr__())


plugin_pool.register_plugin(TimedContent)

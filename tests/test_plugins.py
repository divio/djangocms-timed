# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import core
from django.test import TestCase
from django.utils import timezone

from cms import api

from djangocms_timed.models import TimedContentPlugin


class TimedContentTestCase(TestCase):

    def setUp(self):
        tz_base = timezone.now()
        self.past1 = tz_base.replace(
            year=2000, month=1, day=1,
            hour=0, minute=0, second=0,
        )
        self.past1s = '01 Jan 2000 00:00'
        self.past2 = tz_base.replace(
            year=2001, month=1, day=1,
            hour=0, minute=0, second=0,
        )
        self.past2s = '01 Jan 2001 00:00'
        self.future1 = tz_base.replace(
            year=2100, month=1, day=1,
            hour=0, minute=0, second=0,
        )
        self.future1s = '01 Jan 2100 00:00'
        self.future2 = tz_base.replace(
            year=2101, month=1, day=1,
            hour=0, minute=0, second=0,
        )
        self.future2s = '01 Jan 2101 00:00'

        page = api.create_page('page', 'page.html', 'en')
        page.rescan_placeholders()  # create placeholders
        self.placeholder = page.placeholders.all()[0]

    def get_plugin(self, start, end):
        return TimedContentPlugin(
            timed_start=start,
            timed_end=end,
        )

    def test_plugin_no_start_no_end(self):
        plugin = self.get_plugin(None, None)
        self.assertTrue(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Always visible'
        )

    def test_form_no_start_no_end(self):
        plugin = self.get_plugin(None, None)
        plugin.clean()

    def test_plugin_start_in_past_no_end(self):
        plugin = self.get_plugin(self.past1, None)
        self.assertTrue(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Visible since {}'.format(self.past1s)
        )

    def test_form_start_in_past_no_end(self):
        plugin = self.get_plugin(self.past1, None)
        plugin.clean()

    def test_plugin_start_in_past_end_in_past(self):
        plugin = self.get_plugin(self.past1, self.past2)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Hidden since {}'.format(self.past2s)
        )

    def test_form_start_in_past_end_in_past(self):
        plugin = self.get_plugin(self.past1, self.past2)
        plugin.clean()

    def test_plugin_start_in_past_end_in_past_reversed(self):
        plugin = self.get_plugin(self.past2, self.past1)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Always hidden',
        )

    def test_form_start_in_past_end_in_past_reversed(self):
        plugin = self.get_plugin(self.past2, self.past1)
        with self.assertRaises(core.exceptions.ValidationError):
            plugin.clean()

    def test_plugin_no_start_end_in_past(self):
        plugin = self.get_plugin(None, self.past1)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Hidden since {}'.format(self.past1s)
        )

    def test_form_no_start_end_in_past(self):
        plugin = self.get_plugin(None, self.past1)
        plugin.clean()

    def test_plugin_start_in_past_end_in_future(self):
        plugin = self.get_plugin(self.past1, self.future1)
        self.assertTrue(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Visible since {} until {}'.format(self.past1s, self.future1s)
        )

    def test_form_start_in_past_end_in_future(self):
        plugin = self.get_plugin(self.past1, self.future1)
        plugin.clean()

    def test_plugin_start_in_future_no_end(self):
        plugin = self.get_plugin(self.future1, None)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Hidden until {}'.format(self.future1s)
        )

    def test_form_start_in_future_no_end(self):
        plugin = self.get_plugin(self.future1, None)
        plugin.clean()

    def test_plugin_start_in_future_end_in_past(self):
        plugin = self.get_plugin(self.future1, self.past1)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Always hidden'
        )

    def test_form_start_in_future_end_in_past(self):
        plugin = self.get_plugin(self.future1, self.past1)
        with self.assertRaises(core.exceptions.ValidationError):
            plugin.clean()

    def test_plugin_start_in_future_end_in_future(self):
        plugin = self.get_plugin(self.future1, self.future2)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Hidden until {}'.format(self.future1s)
        )

    def test_form_start_in_future_end_in_future(self):
        plugin = self.get_plugin(self.future1, self.future2)
        plugin.clean()

    def test_plugin_start_in_future_end_in_future_reversed(self):
        plugin = self.get_plugin(self.future2, self.future1)
        self.assertFalse(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Always hidden',
        )

    def test_form_start_in_future_end_in_future_reversed(self):
        plugin = self.get_plugin(self.future2, self.future1)
        with self.assertRaises(core.exceptions.ValidationError):
            plugin.clean()

    def test_plugin_no_start_end_in_future(self):
        plugin = self.get_plugin(None, self.future1)
        self.assertTrue(plugin.is_visible)
        self.assertEqual(
            plugin.get_display(),
            'Visible until {}'.format(self.future1s)
        )

    def test_form_no_start_end_in_future(self):
        plugin = self.get_plugin(None, self.future1)
        plugin.clean()

    def get_plugin_in_page(self, start, end):
        return api.add_plugin(
            placeholder=self.placeholder,
            plugin_type='TimedContent',
            language='en',
            position='last-child',
            timed_start=start,
            timed_end=end,
        )

    def test_get_short_description(self):
        plugin = self.get_plugin_in_page(None, None)
        self.assertEqual(
            plugin.get_short_description(),
            'Always visible'
        )

    def test_plugin_render(self):
        plugin = self.get_plugin_in_page(None, None)
        plugin.render_plugin()

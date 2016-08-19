# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimedContentPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_timed_timedcontentplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('timed_start', models.DateTimeField(null=True, verbose_name='Visible since', blank=True)),
                ('timed_end', models.DateTimeField(null=True, verbose_name='Visible until', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

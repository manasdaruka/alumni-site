# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161219_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ln_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.IntegerField(blank=True, choices=[(2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016')], default=2016),
        ),
    ]

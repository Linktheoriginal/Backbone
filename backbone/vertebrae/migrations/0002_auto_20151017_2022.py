# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vertebrae', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(error_messages={'max_length': 'way too long'}, max_length=200),
        ),
    ]

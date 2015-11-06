# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vertebrae', '0002_auto_20151017_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=8000)),
            ],
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

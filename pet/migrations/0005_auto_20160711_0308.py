# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_auto_20160711_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='birthdate',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]

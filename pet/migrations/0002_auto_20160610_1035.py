# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petpicturecomment',
            name='text',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
    ]

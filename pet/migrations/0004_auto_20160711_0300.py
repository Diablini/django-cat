# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_auto_20160616_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='animal_type',
            field=models.CharField(max_length=10, choices=[(b'cat', b'\xd0\x9a\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'), (b'dog', b'\xd0\x9a\xd1\x83\xd1\x87\xd0\xb5'), (b'otro', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe')]),
            preserve_default=True,
        ),
    ]

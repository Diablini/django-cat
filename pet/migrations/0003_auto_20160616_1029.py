# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_auto_20160610_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='age',
            new_name='birthdate',
        ),
    ]

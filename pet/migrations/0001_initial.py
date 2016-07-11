# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userinfo', '0002_auto_20160528_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('animal_type', models.CharField(max_length=4, choices=[(b'cat', b'\xd0\x9a\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'), (b'dog', b'\xd0\x9a\xd1\x83\xd1\x87\xd0\xb5'), (b'otro', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe')])),
                ('age', models.DateField()),
                ('gender', models.BooleanField(default=True, choices=[(True, b'\xd0\x9c\xd1\x8a\xd0\xb6\xd0\xba\xd0\xb8'), (False, b'\xd0\x96\xd0\xb5\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8')])),
                ('breed', models.CharField(max_length=32)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(to='userinfo.myUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='petPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, null=True)),
                ('img', models.ImageField(upload_to=b'')),
                ('src', models.ForeignKey(to='pet.pet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='petPictureComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=512)),
                ('src', models.ForeignKey(to='pet.petPicture')),
                ('usr', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropBoxAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_key', models.CharField(max_length=100)),
                ('app_secret', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
    ]

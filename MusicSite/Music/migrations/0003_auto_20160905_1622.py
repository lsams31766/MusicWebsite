# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_dropboxaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songfile',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='file_name',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SongFile',
        ),
    ]

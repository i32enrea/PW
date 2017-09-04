# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='votos',
        ),
        migrations.AddField(
            model_name='partido',
            name='escanyos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='votos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

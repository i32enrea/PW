# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dias', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('desplazamiento', models.CharField(default=b'Tren', max_length=7, choices=[(b'Tren', b'Tren'), (b'Avion', b'Avion'), (b'Barco', b'Barco'), (b'Autobus', b'Autobus')])),
                ('destino', models.ForeignKey(related_name=b'viajes', to='viajes.Destino')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

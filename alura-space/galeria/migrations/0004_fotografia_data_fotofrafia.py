# Generated by Django 4.1 on 2024-07-03 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotofrafia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0014_teamlogos'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='image',
            field=models.ImageField(null=True, upload_to=b'profile', blank=True),
            preserve_default=True,
        ),
    ]

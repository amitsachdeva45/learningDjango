# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classBasedView', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['-timestamp', '-id']},
        ),
        migrations.AlterField(
            model_name='class',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customermodel_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='uuid',
            field=uuidfield.fields.UUIDField(max_length=32, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]

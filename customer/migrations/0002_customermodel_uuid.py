# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='uuid',
            field=uuidfield.fields.UUIDField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]

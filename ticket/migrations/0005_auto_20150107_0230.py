# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20150107_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketmodel',
            name='customer',
        ),
        migrations.AddField(
            model_name='ticketmodel',
            name='customer_uuid',
            field=uuidfield.fields.UUIDField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]

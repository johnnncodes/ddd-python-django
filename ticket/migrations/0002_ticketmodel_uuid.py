# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmodel',
            name='uuid',
            field=uuidfield.fields.UUIDField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]

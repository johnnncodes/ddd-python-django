# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20150107_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='email_address',
            field=models.EmailField(unique=True, max_length=254),
            preserve_default=True,
        ),
    ]

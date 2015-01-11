# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('ticket', '0002_ticketmodel_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmodel',
            name='customer',
            field=models.ForeignKey(related_name='tickets', default=1, to='customer.CustomerModel'),
            preserve_default=False,
        ),
    ]

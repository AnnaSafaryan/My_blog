# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='header',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]

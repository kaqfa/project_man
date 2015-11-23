# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlog',
            name='status',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'Not Ready'), (b'P', b'In Progress'), (b'F', b'Finished'), (b'T', b'Ready to Test')]),
        ),
    ]

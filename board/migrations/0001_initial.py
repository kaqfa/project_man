# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import taggit.managers
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component', models.CharField(max_length=200)),
                ('data', models.TextField(null=True, blank=True)),
                ('testing', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='backlog',
            name='board',
            field=models.ForeignKey(to='board.Board'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='end_user',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='board.Backlog', null=True),
        ),
    ]

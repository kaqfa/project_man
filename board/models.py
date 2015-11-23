from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Board(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class Backlog(MPTTModel):
    end_user = TaggableManager()
    component = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    data = models.TextField(null=True, blank=True)
    testing = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # label = TaggableManager()
    board = models.ForeignKey(Board)

    class MPTTMeta:
        order_insertion_by = ['component']

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Backlog(models.Model):
    end_user = TaggableManager()
    component = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    data = models.TextField(null=True, blank=True)
    testing = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    label = TaggableManager()

    class Meta:
        order_insertion_by = ['component']

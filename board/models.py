from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Board(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def num_of_backlog(self):
        return self.backlog_set.all().count()

    def num_finished_backlog(self):
        return self.backlog_set.filter(status='F').count()

    def num_ready_to_test_backlog(self):
        return self.backlog_set.filter(status='T').count()

    def __unicode__(self):
        return self.title


class Backlog(MPTTModel):
    STATUS_CHOICE = (
            ('N', 'Not Ready'),
            ('P', 'In Progress'),
            ('F', 'Finished'),
            ('T', 'Ready to Test'),
        )
    end_user = TaggableManager()
    component = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    description = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    testing = models.TextField(null=True, blank=True)
    # label = TaggableManager()
    board = models.ForeignKey(Board)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='N')

    def __unicode__(self):
        return self.component

    class MPTTMeta:
        order_insertion_by = ['component']

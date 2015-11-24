from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableModelAdmin
from suit.widgets import AutosizedTextarea
from django.forms import ModelForm

from .models import Board, Backlog


class BacklogForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'class': 'span12'}),
            'data': AutosizedTextarea(attrs={'class': 'span12'}),
            'testing': AutosizedTextarea(attrs={'class': 'span12'}),
        }


class BacklogInline(admin.StackedInline):
    model = Backlog
    fields = ('component', 'description', 'data', 'testing', 'status')
    extra = 1
    form = BacklogForm


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'num_of_backlog',
                    'num_finished_backlog', 'num_ready_to_test_backlog')
    inlines = (BacklogInline,)


class BacklogAdmin(MPTTModelAdmin):
    list_display = ('component', 'description', 'data', 'testing', 'board', 'status')
    list_filter = ('board__title', 'status', 'component')
    search_fields = ['component']
    mptt_level_indent = 15
    form = BacklogForm

#    def suit_row_attributes(self, obj, request):
#        class_map = {
#            'Finished': 'success',
#            'In Progress': 'warning',
#            'Not Ready': 'error',
#            'Ready to Test': 'info',
#        }
#
#        css_class = class_map.get(obj.status)
#        if css_class:
#            return {'class': css_class}


admin.site.register(Board, BoardAdmin)
admin.site.register(Backlog, BacklogAdmin)

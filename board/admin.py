from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableModelAdmin

from .models import Board, Backlog


class BacklogInline(admin.StackedInline):
    model = Backlog
    fields = ('component', 'description', 'data', 'testing', 'status')
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'num_of_backlog',
                    'num_finished_backlog', 'num_ready_to_test_backlog')
    inlines = (BacklogInline,)


class BacklogAdmin(MPTTModelAdmin):
    list_display = ('component', 'description', 'data', 'testing', 'board', 'status')
    list_filter = ('board__title', 'status', 'component')
    search_fields = ['component']
    mptt_level_indent = 15

    def suit_row_attributes(self, obj, request):
        class_map = {
            'Finished': 'success',
            'In Progress': 'warning',
            'Not Ready': 'error',
            'Ready to Test': 'info',
        }

        css_class = class_map.get(obj.status)
        if css_class:
            return {'class': css_class}


admin.site.register(Board, BoardAdmin)
admin.site.register(Backlog, BacklogAdmin)

from django.contrib import admin
from .models import Board, Backlog


class BacklogInline(admin.StackedInline):
    model = Backlog
    fields = ('component', 'description', 'data', 'testing', 'status')
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'num_of_backlog',
                    'num_finished_backlog', 'num_ready_to_test_backlog')
    inlines = (BacklogInline,)


class BacklogAdmin(admin.ModelAdmin):
    list_display = ('component', 'description', 'data', 'testing', 'board', 'status')
    list_filter = ('board__title', 'status', 'component')
    search_fields = ['component']


admin.site.register(Board, BoardAdmin)
admin.site.register(Backlog, BacklogAdmin)

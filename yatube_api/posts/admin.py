# posts/admin.py
from django.contrib import admin
from posts.models import Group


class GroupAdmin(admin.ModelAdmin):
    """Отображение групп в админке."""

    list_display = ('pk',
                    'title',
                    'slug',
                    'description',
                    )
    empty_value_displey = '-пусто-'


admin.site.register(Group, GroupAdmin)

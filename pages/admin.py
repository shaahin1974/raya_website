from django.contrib import admin

from .models import ServiceArea


class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'description', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 25


admin.site.register(ServiceArea, PagesAdmin)

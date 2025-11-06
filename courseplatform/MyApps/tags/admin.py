from django.contrib import admin
from MyApps.tags.models import Tags

# Register your models here.

class TagsAdmin(admin.ModelAdmin):
    list_display= ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Tags,TagsAdmin)
from django.contrib import admin
from MyApps.users.models import Students,Teachers

# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'specialty')
    list_filter = ('specialty',)
    search_fields = ('name', 'last_name', 'email', 'specialty')
    ordering = ('name', 'last_name')

    fieldsets = (
        ('Información Personal', {
            'fields': ('name', 'last_name', 'email', 'phone')
        }),
        ('Detalles Profesionales', {
            'fields': ('specialty', 'biography', 'photo_url')
        }),
    )


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'last_name', 'email')
    ordering = ('name', 'last_name')

    fieldsets = (
        ('Información Personal', {
            'fields': ('name', 'last_name', 'email', 'phone', 'photo_url')
        }),
        ('Estado', {
            'fields': ('state',),
        }),
    )

admin.site.register(Students, StudentsAdmin)
admin.site.register(Teachers, TeachersAdmin)
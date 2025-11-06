from django.contrib import admin
from MyApps.courses.models import Courses, Lessons, Modules, Registrations

# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'state_course', 'start_date', 'end_date', 'level', 'price', 'teacher_id')
    list_filter = ('state_course', 'level', 'start_date', 'end_date', 'language')
    search_fields = ('title', 'description', 'objetives', 'requeriments')
    filter_horizontal = ('tags',)
    ordering = ('creation_date',)

    fieldsets = (
        ('Información del Curso', {
            'fields': ('title', 'description', 'objetives', 'requeriments', 'language')
        }),
        ('Detalles del Curso', {
            'fields': ('creation_date', 'start_date', 'end_date', 'price', 'max_students', 'estimated_duration')
        }),
        ('Configuración Adicional', {
            'fields': ('state_course', 'level', 'certificate_available', 'image_url')
        }),
        ('Relaciones', {
            'fields': ('teacher_id', 'tags'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('creation_date',)



class ModulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'available_date', 'course')
    list_filter = ('available_date', 'course')
    search_fields = ('name', 'description')
    ordering = ('available_date',)

    fieldsets = (
        ('Información del Módulo', {
            'fields': ('name', 'description', 'order')
        }),
        ('Disponibilidad', {
            'fields': ('estimated_duration', 'available_date')
        }),
        ('Relación', {
            'fields': ('course',)
        }),
    )



class LessonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'available_date', 'order', 'id_module')
    list_filter = ('content_type', 'available_date')
    search_fields = ('name', 'content')
    ordering = ('available_date',)

    fieldsets = (
        ('Detalles de la Lección', {
            'fields': ('name', 'content', 'content_type')
        }),
        ('Disponibilidad', {
            'fields': ('available_date', 'order')
        }),
        ('Recursos', {
            'fields': ('resource_url',)
        }),
        ('Relación', {
            'fields': ('id_module',)
        }),
    )



class RegistrationsAdmin(admin.ModelAdmin):
    list_display = ('registration_date', 'state', 'student', 'course', 'final_grade', 'progress')
    list_filter = ('state', 'registration_date', 'course')
    search_fields = ('state', 'student__name')
    ordering = ('registration_date',)

    fieldsets = (
        ('Información de Registro', {
            'fields': ('registration_date', 'state')
        }),
        ('Progreso y Calificación', {
            'fields': ('final_grade', 'certificate_issued', 'progress')
        }),
        ('Relación', {
            'fields': ('student', 'course')
        }),
    )

    readonly_fields = ('registration_date',)

admin.site.register(Courses,CoursesAdmin)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Registrations, RegistrationsAdmin)


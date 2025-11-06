from django.contrib import admin
from MyApps.evaluations.models import Attempts, Evaluations, Deliveries,StudentDeliveries

# Register your models here.

class EvaluationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'maximun_score', 'limit_date', 'lesson')
    list_filter = ('type', 'limit_date', 'available_from', 'available_until')
    search_fields = ('title', 'description', 'type')
    ordering = ('limit_date',)

    fieldsets = (
        ('Detalles de la Evaluación', {
            'fields': ('title', 'description', 'type')
        }),
        ('Configuración de Fechas', {
            'fields': ('available_from', 'available_until', 'limit_date')
        }),
        ('Puntaje y Reglas', {
            'fields': ('maximun_score', 'minimum_score', 'attempts_allowed', 'show_results')
        }),
        ('Relación', {
            'fields': ('lesson',)
        }),
    )



class AttemptsAdmin(admin.ModelAdmin):
    list_display = ('attempt_date', 'attempt_number', 'state', 'score_obtained', 'student', 'evaluation')
    list_filter = ('state', 'attempt_date', 'evaluation')
    search_fields = ('state', 'student__first_name', 'student__last_name')
    ordering = ('attempt_date',)

    fieldsets = (
        ('Información del Intento', {
            'fields': ('attempt_date', 'attempt_number', 'state')
        }),
        ('Tiempos y Calificación', {
            'fields': ('start_time', 'end_time', 'time_spent', 'score_obtained', 'maximun_score')
        }),
        ('Respuestas', {
            'fields': ('answers',),
            'classes': ('collapse',)
        }),
        ('Relaciones', {
            'fields': ('student', 'evaluation')
        }),
    )



class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'limit_date', 'lesson')
    list_filter = ('limit_date',)
    search_fields = ('title', 'description')
    ordering = ('limit_date',)

    fieldsets = (
        ('Información de la Entrega', {
            'fields': ('title', 'description')
        }),
        ('Fecha Límite', {
            'fields': ('limit_date',)
        }),
        ('Relación', {
            'fields': ('lesson',)
        }),
    )


class StudentDeliveriesAdmin(admin.ModelAdmin):
    list_display = ('state', 'delivery_date', 'calification', 'student', 'delivery')
    list_filter = ('state', 'delivery_date', 'student')
    search_fields = ('student__first_name', 'student__last_name', 'state')
    ordering = ('delivery_date',)

    fieldsets = (
        ('Detalles de la Entrega del Estudiante', {
            'fields': ('delivery_date', 'archive', 'calification', 'state')
        }),
        ('Relaciones', {
            'fields': ('student', 'delivery')
        }),
    )

admin.site.register(Attempts, AttemptsAdmin)
admin.site.register(Evaluations, EvaluationsAdmin)
admin.site.register(Deliveries, DeliveriesAdmin)
admin.site.register(StudentDeliveries, StudentDeliveriesAdmin)
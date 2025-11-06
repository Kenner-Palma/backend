from django.contrib import admin
from MyApps.community.models import Posts, Forums

# Register your models here.
class ForumsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'date', 'is_moderated', 'is_active', 'course')
    list_filter = ('type', 'is_moderated', 'is_active', 'date')
    search_fields = ('title', 'description')
    list_editable = ('is_moderated','is_active')
    ordering = ('title','type')
    
    fieldsets = (
        ('Informacion del Foro', {
            'fields': ('title', 'type', 'course')
        }),
        ('Estado activo', {
            'fields': ('is_active', 'is_moderated')
        })
    )

    # Solo mostrar campos de solo lectura para el password en el formulario de cambio
    readonly_fields = ()

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # Editando un cliente existente
    #         return ('email',)  # Email no editable una vez creado por la constraint unique
    #     return ()
    
class PostsAdmin(admin.ModelAdmin):
    list_display = ('content', 'publications_date', 'is_question', 'is_accepted_answer', 'upvotes', 'downvotes', 'forum', 'student', 'teacher', 'post_father')
    list_filter = ('is_question', 'is_accepted_answer', 'is_moderated', 'publications_date')
    search_fields = ('content',)
    list_editable = ('forum', 'student', 'teacher', 'post_father')
    ordering = ('publications_date','content')

    fieldsets = (
        ('Información del Post', {
            'fields': ('content', 'forum', 'student', 'teacher', 'post_father')
        }),
        ('Detalles del Post', {
            'fields': ('is_question', 'is_accepted_answer', 'upvotes', 'downvotes')
        }),
        ('Moderación', {
            'fields': ('is_moderated',)
        }),
    )


admin.site.register(Forums,ForumsAdmin)
admin.site.register(Posts, PostsAdmin)
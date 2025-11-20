from django.db import models
from MyApps.users.models import Students, Teachers
from MyApps.courses.models import Courses


# Create your models here.
class Forums(models.Model):
    TYPE_CHOICES = [
        ('GENERAL','General'),
        ('PREGUNTA','Pregunta'),
        ('PROJECTOS','Projectos'),
        ('SOCIAL','Social')
    ]
    
    title = models.CharField(max_length=200, help_text="Digite el titulo del Foro")
    description = models.TextField(help_text="Describa el tema principal del foro")
    type = models.CharField(
        max_length=9, 
        choices= TYPE_CHOICES,
        blank=True,
        null=True,
        help_text="Seleccione el tipo de foro")
    date = models.DateTimeField(auto_now_add= True, help_text="Digite la fecha y hora del Foro")
    is_moderated = models.BooleanField(default= False, blank=True, help_text="Indique si los mensajes en el foro deben aprobarse antes de publicarse")
    is_active = models.BooleanField(default= False, blank= True, help_text="Indique si el foro está activo o desactivado")
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE, 
        help_text="Seleccione el curso"
        , blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'forums'
        verbose_name = "forum"
        verbose_name_plural = "forums"
        
        
class Posts(models.Model):
    content = models.TextField(help_text="Digite el Contenido del post o mensaje")
    publications_date = models.DateTimeField( auto_now_add=True, help_text="Digite Fecha y hora en que se creó el post")
    attachment_url = models.CharField(max_length=255, blank=True, null=True, help_text="URL del archivo adjunto (si aplica)")
    is_question = models.BooleanField(default= False , help_text="Indique si este post es una pregunta")
    is_accepted_answer = models.BooleanField(default= False, help_text="Indique si la respuesta ha sido aceptada como solución")
    upvotes = models.IntegerField(default= 0, help_text="Digite Número de votos positivos que ha recibido el post")
    downvotes = models.IntegerField(default= 0, help_text="Digite Número de votos negativos que ha recibido el post")
    is_moderated = models.BooleanField(default= False, help_text="Indique si el post está pendiente de aprobación")
    published_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="Fecha de publicación del post")
    edited_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="Fecha de la última edición del post")
    forum = models.ForeignKey(
        Forums, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el foro"
        , blank=True, null=True)
    student = models.ForeignKey(
        Students, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el estudiante"
        , blank=True, null=True)
    teacher = models.ForeignKey(
        Teachers, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el profesor"
        , blank=True, null=True)
    post_father = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        help_text="Seleccione el posts"
        , blank=True, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'posts'
        verbose_name = "post"
        verbose_name_plural = "posts"

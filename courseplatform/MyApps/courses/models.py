from django.db import models
from MyApps.users.models import Teachers, Students
from MyApps.tags.models import Tags

# Create your models here.
class Courses(models.Model):
    
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('archivado', 'Archivado'),
    ]

    NIVEL_CHOICES = [
        ('básico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    
    title= models.CharField(max_length=200, help_text="Ingrese el titulo del Curso")
    description = models.TextField(help_text="Ingrese la descripcion del Curso")
    objetives = models.TextField(help_text="Ingrese los objetivos del Curso")
    creation_date = models.DateField(auto_created=True, help_text="Ingrese la fecha de creacion del Curso")
    start_date = models.DateField(help_text="Ingrese la fecha de inicio del Curso")
    end_date = models.DateField(help_text="Ingrese la fecha de finalizacion del Curso")
    state_course = models.CharField(max_length=100, help_text="Selecciona el estado del Curso", choices = ESTADO_CHOICES)
    requeriments = models.CharField(max_length=50, blank=True, null=True , help_text="Ingrese los requerimientos del curso")
    language = models.CharField(max_length=15 , help_text="Ingrese el idioma del curso")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Ingrese el precio del curso")
    max_students = models.IntegerField(blank=True, null=True, help_text="Ingrese el maximo de estudiantes del curso")
    level = models.CharField(max_length=15, choices=NIVEL_CHOICES, help_text="Seleccione el nivel del curso")
    image_url = models.CharField(max_length=255, blank=True, null=True, help_text="Ingrese una imagen para el curso")
    certificate_available = models.BooleanField(default=False, help_text="Indique si tiene cetificado disponible el curso")
    estimated_duration = models.IntegerField(blank=True, null=True, help_text="Ingrese la duracion del curso")
    teacher_id = models.ForeignKey(
        Teachers,  # o el nombre del modelo relacionado
        on_delete=models.CASCADE,
        help_text="Seleccione el profesor asociado al curso"
    )
    
    tags = models.ManyToManyField(
        Tags, 
        related_name='courses', 
        blank=True,
        help_text="Seleccione los tags asociados al curso"
    )
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = "courses"  
        verbose_name = "course"
        verbose_name_plural = "courses"

class Modules(models.Model):
    name = models.CharField(max_length=50, help_text= "Ingrese el nombre del Modulo")
    description = models.TextField( help_text= "Ingrese la descripcion del Modulo")
    order = models.CharField(max_length=100, help_text= "Ingrese el orden del Modulo")
    estimated_duration = models.IntegerField(blank=True, null=True, help_text= "Ingrese la duracion estimada del Modulo")
    available_date = models.DateField(blank=True, null=True, help_text= "Ingrese la fecha de disponibilidad del Modulo")
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE, 
        help_text="Seleccione el Curso asociado al Modulo")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'modules'
        verbose_name = 'module'
        verbose_name_plural = 'modules'


class Lessons(models.Model):
    name = models.CharField(max_length=100, help_text="Ingrese el nombre de la lección")
    content = models.TextField(help_text="Ingrese el contenido de la lección")
    content_type = models.CharField(max_length=14, help_text="Ingrese el tipo de contenido")
    available_date = models.DateField(blank=True, null=True, help_text="Ingrese la fecha de disponibilidad de la lección")
    order = models.CharField(max_length=50, help_text="Ingrese el orden de la lección dentro del módulo")
    resource_url = models.CharField(max_length=255, blank=True, null=True, help_text="Ingrese la URL del recurso asociado")
    id_module = models.ForeignKey(
        Modules, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el Modulo" )
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lessons'
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        

class Registrations(models.Model):
    REGISTRATION_STATE_CHOICES = [
        ('active', 'Activo'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]

    registration_date = models.DateTimeField(help_text="Ingrese la fecha y hora de la Inscripcion")
    state = models.CharField(max_length=10, choices= REGISTRATION_STATE_CHOICES, help_text="Seleccione el estado de la Inscripcion")
    final_grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Ingrese la calificación final del estudiante")
    certificate_issued = models.BooleanField(blank=True, null=True, help_text="Indique si se emitió el certificado")
    progress = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Ingrese el progreso del estudiante en el curso en porcentaje")
    student = models.ForeignKey(
            Students, 
            on_delete=models.CASCADE, 
            help_text="Seleccione el estudiante")
    course = models.ForeignKey(
            Courses,
            on_delete=models.CASCADE, 
            help_text="Seleccione el curso")
    
    def __str__(self):
        return f'{self.registration_date}, {self.state}'

    class Meta:
        db_table = 'registrations'
        verbose_name = 'registration'
        verbose_name_plural = 'registrations'
from django.db import models
from MyApps.users.models import Students
from MyApps.courses.models import Lessons


# Create your models here.
class Evaluations(models.Model):
    TYPE_CHOICES=[
        ('Exam', 'Exam'),
        ('Quiz', 'Quiz'),
        ('Assigment','Assignment')
    ]
    title = models.CharField(max_length=30, help_text="Ingrese el título de la evaluación")
    description = models.TextField(help_text="Ingrese la descripción de la evaluación")
    type = models.CharField(
        max_length=10, 
        choices= TYPE_CHOICES,
        help_text="Ingrese el tipo de evaluación (ej. Quiz, Tarea, Examen)")
    maximun_score = models.IntegerField(blank=True, null=True, help_text="Ingrese la calificación máxima posible")
    limit_date = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha límite para completar la evaluación")
    available_from = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha desde la cual estará disponible la evaluación")
    available_until = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha hasta la cual estará disponible la evaluación")
    show_results = models.BooleanField(blank=True, null=True, help_text="Indique si se muestran los resultados inmediatamente")
    minimum_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Ingrese la calificación mínima para aprobar la evaluación")
    attempts_allowed = models.IntegerField(blank=True, null=True, help_text="Ingrese el número máximo de intentos permitidos")
    lesson = models.ForeignKey(
        Lessons, 
        on_delete=models.CASCADE, 
        help_text="Seleccione la leccion" )
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'evaluations'
        verbose_name = 'evaluation'
        verbose_name_plural = 'evaluations'
        
        
class Attempts(models.Model):
    STATE_CHOICES= [
        ('EN PROGRESO', 'en progreso'),
        ('COMPLETADO', 'completado'),
        ('CALIFICADO', 'calificado'),
    ]
    
    
    attempt_date = models.DateTimeField(help_text="Ingrese la fecha y hora del intento")
    attempt_number = models.IntegerField(blank=True, null=True, help_text="Ingrese el número del intento")
    start_time = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha y hora de inicio del intento")
    end_time = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha y hora de finalización del intento")
    time_spent = models.IntegerField(blank=True, null=True, help_text="Ingrese el tiempo total dedicado al intento (en minutos)")
    state = models.CharField(
        max_length=11,
        choices=STATE_CHOICES,
        help_text="Ingrese el estado del intento (ej. completado, en progreso)")
    maximun_score = models.IntegerField(blank=True, null=True, help_text="Ingrese la calificación máxima del intento")
    score_obtained = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True, help_text="Ingrese la calificación obtenida en el intento")
    answers = models.JSONField(blank=True, null=True, help_text="Ingrese las respuestas dadas por el estudiante (en formato JSON)")
    evaluation = models.ForeignKey(
        Evaluations, 
        on_delete=models.CASCADE, 
        help_text="Seleccione la evaluacion relacionada con el intento"
        , blank=True, null=True)
    student = models.ForeignKey(
        Students, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el estudiante que realizo el intento"
        , blank=True, null=True)
    
    def __str__(self):
        return f'{self.attempt_date}, {self.attempt_number}'

    class Meta:
        db_table = 'attempts'
        verbose_name = "attempt"
        verbose_name_plural = "attempts"
        
        
class Deliveries(models.Model):
    title = models.TextField(help_text="Ingrese el título de la entrega")
    description = models.TextField(help_text="Ingrese la descripción de la entrega")
    limit_date = models.DateTimeField(blank=True, null=True, help_text="Ingrese la fecha límite de la entrega")
    lesson = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        help_text="Seleccione la lección relacionada con la entrega"
    )

    class Meta:
        db_table = 'deliveries'
        verbose_name = "deliverie"
        verbose_name_plural = "deliveries"
        
class StudentDeliveries(models.Model):
    STATE_CHOICES=[
        ('CALIFICADO', 'Calificado'),
        ('PENDIENTE', 'Pendiente'),
        ('DEVUELTA', 'Devuelta')
    ]
    delivery_date = models.DateTimeField(help_text="Ingrese la fecha en que el estudiante realizó la entrega")
    archive = models.CharField(max_length=255, help_text="Ingrese la URL o ruta del archivo entregado por el estudiante")
    calification = models.FloatField(help_text="Ingrese la calificación obtenida en la entrega")
    state = models.CharField(
        max_length=20,
        choices= STATE_CHOICES,
        help_text="Indique el estado de la entrega")

    delivery = models.ForeignKey(
        Deliveries,
        on_delete=models.CASCADE,
        help_text="Seleccione la entrega relacionada",
        blank=True, null=True
    )
    student = models.ForeignKey(
        Students,
        on_delete=models.CASCADE,
        help_text="Seleccione el estudiante que realizó la entrega",
        blank=True, null=True
    )
    
    class Meta:
        db_table = 'student_deliveries'
        verbose_name = "student_deliverie"
        verbose_name_plural = "student_deliveries"
        
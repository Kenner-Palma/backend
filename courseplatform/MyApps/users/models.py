from django.db import models

# Create your models here.
class Teachers(models.Model):
        name = models.CharField( max_length=50, help_text="Ingrese el nombre del Profesor")
        last_name = models.CharField(max_length=50, help_text = "Ingrese el apellido del Profesor")
        email = models.CharField(max_length=100, help_text = "Ingrese el correo del Profesor")
        phone = models.CharField(max_length=20, blank=True, null=True, help_text = "Ingrese el numero de telefono del Profesor")
        specialty = models.CharField(max_length=100, help_text = "Ingrese la especialidad del Profesor")
        biography = models.TextField(help_text = "Ingrese la biografia del Profesor")
        photo_url = models.CharField(max_length=250, blank=True, null=True, help_text = "Ingrese la URL de la foto del Profesor")
        
        def __str__(self):
                return self.name
        
        class Meta:
                db_table = 'teachers'
                verbose_name = 'teacher'
                verbose_name_plural = "teachers"
                
class Students(models.Model):    
    STATE_CHOICES=[
        ('ACTIVO','Activo'),
        ('INACTIVO','Inactivo'),
        ('SUSPENDIDO','suspendido')
    ]
    
    name = models.CharField(max_length=50, help_text="Ingrese el nombre del Estudiante")
    last_name = models.CharField(max_length=50, help_text="Ingrese el apellido del Estudiante")
    email = models.CharField(max_length=30, help_text="Ingrese el Correo del Estudiante")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Ingrese el numero de telefono del Estudiante")
    state = models.CharField(
            max_length=10,
            choices= STATE_CHOICES,
            help_text="Indique el estado del Estudiante")
    photo_url = models.CharField(max_length=250, blank=True, null=True, help_text="Ingrese el URL de la foto del Estudiante")
    
    def __str__(self):
          return f'{self.name}, {self.last_name}'

    class Meta:
        db_table = 'students'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        

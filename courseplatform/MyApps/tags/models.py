from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=30, help_text="Ingrese el nombre del Tag")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = "tag"
        verbose_name_plural = "tags"
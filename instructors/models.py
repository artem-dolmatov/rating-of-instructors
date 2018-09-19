from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")

    def __str__(self):
        return "Имя %s" %(self.name)

    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"
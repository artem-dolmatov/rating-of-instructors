from django.db import models
from django.urls import reverse

# Create your models here.
class Instructor(models.Model):
    CHOISE_SCHOOL = (
        ('formula', 'Формула'),
    )
    CHOISE_CITY = (
        ('tymen', 'Тюмень'),
    )
    CHOISE_TRANSMISSION = (
        ('mkpp', 'МКПП'),
        ('akpp', 'АКПП'),
    )
    CHOISE_GENDER = (
        ('men', 'Мужской'),
        ('women', 'Женский'),
    )
    CHOISE_HOUR = (
        ('45 min', '45 мин'),
        ('60 min', '60 мин'),
    )

    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    name               = models.CharField(max_length=20, verbose_name="Имя")
    patronymic         = models.CharField(max_length=20, verbose_name="Отчество")
    age                = models.IntegerField(verbose_name="Возраст")
    driving_experience = models.DateField(auto_now=False, verbose_name="Стаж вождения c")
    experience         = models.DateField(auto_now=False, verbose_name="Проф. стаж c")
    school             = models.CharField(max_length=20, verbose_name="Автошкола", choices=CHOISE_SCHOOL)
    city               = models.CharField(max_length=20, verbose_name="Город", choices=CHOISE_CITY)
    car                = models.CharField(max_length=20, verbose_name="Автомобиль")
    transmission       = models.CharField(max_length=20, verbose_name="Коробка передач", choices=CHOISE_TRANSMISSION)
    category           = models.CharField(max_length=20, verbose_name="Категория")
    gender             = models.CharField(max_length=20, verbose_name="Пол", choices=CHOISE_GENDER)
    phone              = models.CharField(max_length=20, verbose_name="Телефон")
    price_hour         = models.IntegerField(verbose_name="Стоимость часа")
    length_of_hour     = models.CharField(max_length=10, verbose_name="Продолжительность часа", choices=CHOISE_HOUR)
    description        = models.TextField(max_length=200, verbose_name="Описание")

    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"

    def get_absolute_url(self):
        return reverse('instructor_detail', args=[str(self.id)])
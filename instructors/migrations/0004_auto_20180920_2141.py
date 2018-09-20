# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_auto_20180920_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='description',
            field=models.TextField(default='exit', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='category',
            field=models.CharField(max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='driving_experience',
            field=models.DateField(verbose_name='Стаж вождения c'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='experience',
            field=models.DateField(verbose_name='Проф. стаж c'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='length_of_hour',
            field=models.CharField(choices=[('45 min', '45 мин'), ('60 min', '60 мин')], max_length=10, verbose_name='Продолжительность часа'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='school',
            field=models.CharField(choices=[('formula', 'Формула')], max_length=20, verbose_name='Автошкола'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='transmission',
            field=models.CharField(choices=[('mkpp', 'МКПП'), ('akpp', 'АКПП')], max_length=20, verbose_name='Коробка передач'),
        ),
    ]

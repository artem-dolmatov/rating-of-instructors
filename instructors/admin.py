from django.contrib import admin
from . import models

# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Instructor._meta.fields]

admin.site.register(models.Instructor, InstructorAdmin)
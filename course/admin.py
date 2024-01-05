from django.contrib import admin
from .models import Course

# admin.py

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

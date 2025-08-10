from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','updated_at','created_at',)

admin.site.register(Student,StudentAdmin)
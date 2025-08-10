from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) #this will save the date when user created and cannot be changed
    updated_at = models.DateTimeField(auto_now=True) #this will save the date when user info was updated and can be changed


    def __str__(self):
        return self.name
    
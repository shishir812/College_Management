from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    year = models.IntegerField()
    mail = models.EmailField()
    phone = models.CharField(max_length=100)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
class Students(models.Model):
    stdId = models.CharField(max_length=10, primary_key=True)
    stdName = models.CharField(max_length=50)
    stdYear = models.IntegerField()
    stdCourse = models.CharField(max_length=5)
    
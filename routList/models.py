from django.db import models
from django.contrib.auth.models import User

class rout(models.Model):
    rout_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    setter = models.CharField(max_length=100)
    date_set = models.DateField()
    climbed = models.CharField(max_length=1)
    date_climbed = models.DateField(blank=True, null=True)
    attempts = models.IntegerField(blank=True)
    notes = models.TextField(default="No notes")

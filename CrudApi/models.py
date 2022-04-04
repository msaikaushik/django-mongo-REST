from django.db import models
from django.forms import JSONField

class User(models.Model):
    name = models.CharField(max_length=70, blank=False, default='',unique=True)
    data = models.JSONField()
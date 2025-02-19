from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class TodoListItem(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(blank=False, null=False)
    completed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
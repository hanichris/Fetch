from django.db import models

# Create your models here.

class Posts(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField()
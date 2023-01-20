from django.db import models

# Create your models here.

class Fruit(models.Model):
    data = models.JSONField()

    def __str__(self):
        return self.data.get('name', '-')

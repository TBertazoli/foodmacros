from django.db import models
from django.urls import reverse

# Create your models here.


class Add_Food(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tracker', kwargs={'pk': self.id})

from django.db import models
from django.urls import reverse

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})

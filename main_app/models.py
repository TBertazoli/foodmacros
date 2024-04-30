from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.


class Add_Food(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    date = models.DateField()
    meal = models.CharField(
        choices=MEALS,
        default=MEALS[0][0])

    def __str__(self):
        return f'{self.name} ({self.id}) {self.get_meal_display()} on {self.date}'

    def get_absolute_url(self):
        return reverse('tracker', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date']

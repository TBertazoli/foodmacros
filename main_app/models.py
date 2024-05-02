from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.


class Add_Food(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    date = models.DateField(default=date.today)
    meal = models.CharField(
        choices=MEALS,
        default=MEALS[0][0])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id}) {self.get_meal_display()} on {self.date}'

    def get_absolute_url(self):
        return reverse('account')

    class Meta:
        ordering = ['-date']

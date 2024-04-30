from django import forms
from django.forms import ModelForm
from .models import Add_Food


class AddFoodForm(ModelForm):
    class Meta:
        model = Add_Food
        fields = ['name', 'weight', 'calories',
                  'protein', 'fat', 'carbs', 'meal', 'date']

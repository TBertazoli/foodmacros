from js.jquery import jquery
from django.shortcuts import render, redirect
import requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import os
from dotenv import load_dotenv
from .models import Add_Food
from .forms import AddFoodForm
jquery.need()
load_dotenv()


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def account(request):
    return render(request, 'account/index.html')


def tracker(request):
    foods = Add_Food.objects.all()
    return render(request, 'account/tracker.html', {
        'foods': foods

    })


def search(request):
    api_key = os.getenv('APPLICATION_KEY')
    api_id = os.getenv('APPLICATION_ID')
    search = request.GET.get('food-search')
    url = "https://api.edamam.com/api/food-database/v2/parser?app_id=" + \
        api_id + "&app_key=" + api_key + "&ingr=" + search + "&nutrition-type=cooking"

    response = requests.get(url)
    data = response.json()
    foods = Add_Food.objects.all()
    print(data)
    return render(request, 'account/tracker.html', {'data': data, 'foods': foods})


def food_create(request):
    foods = Add_Food.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = AddFoodForm(request.POST)
        print('here', form.is_valid(), form.errors)
        if form.is_valid():
            form.save()
        return render(request, 'account/tracker.html', {'foods': foods})


class FoodDelete(DeleteView):
    model = Add_Food
    success_url = '/account/tracker'


def food_update(request, pk):
    food = Add_Food.objects.get(pk=pk)
    return render(request, 'account/food_form.html', {
        'food': food
    })


def food_save(request, pk):
    foods = Add_Food.objects.all()
    food = Add_Food.objects.get(pk=pk)
    if request.method == 'POST':
        food.save()
    return render(request, 'account/tracker.html', {'foods': foods})


class FoodUpdate(UpdateView):
    model = Add_Food
    fields = ['weight', 'meal', 'date']
    success_url = '/account/tracker'

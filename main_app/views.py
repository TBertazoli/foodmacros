from django.shortcuts import render, redirect
import requests
from django.views.generic import ListView, DetailView
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from .models import Search_Food
load_dotenv()


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def account(request):
    # response = get_url(request)
    return render(request, 'foods/index.html')


def search(request):
    api_key = os.getenv('APPLICATION_KEY')
    api_id = os.getenv('APPLICATION_ID')
    search = request.GET.get('food-search')
    url = "https://api.edamam.com/api/food-database/v2/parser?app_id=" + \
        api_id + "&app_key=" + api_key + "&ingr=" + search + "&nutrition-type=cooking"

    response = requests.get(url)
    data = response.json()
    print(data)
    return render(request, 'foods/index.html', {'data': data})

from js.jquery import jquery
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
import requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os
from dotenv import load_dotenv
from .models import Add_Food
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
jquery.need()
load_dotenv()


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def account(request):
    foods = Add_Food.objects.filter(user=request.user)
    today = date.today().strftime("%Y-%m-%d")
    print(today)
    return render(request, 'account/index.html', {
        'foods': foods,
        'today': today,

    })


def search(request):
    api_key = os.getenv('APPLICATION_KEY')
    api_id = os.getenv('APPLICATION_ID')
    search = request.GET.get('food-search')
    url = "https://api.edamam.com/api/food-database/v2/parser?app_id=" + \
        api_id + "&app_key=" + api_key + "&ingr=" + search + "&nutrition-type=cooking"

    response = requests.get(url)
    data = response.json()
    foods = Add_Food.objects.filter(user=request.user)
    today = date.today().strftime("%Y-%m-%d")
    print(today)
    return render(request, 'account/index.html', {'data': data, 'foods': foods, "today": today})


class DateInput(forms.DateInput):
    input_type = 'date'


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Add_Food
    fields = ['name', 'weight', 'calories',
              'protein', 'fat', 'carbs', 'meal', 'date', 'user']
    widgets = {
        "date": DateInput()
    }

    def for_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Add_Food
    success_url = '/account'


class FoodUpdate(UpdateView):
    model = Add_Food
    fields = ['weight', 'meal', 'date']


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            login(request, user)
            return redirect('/account')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

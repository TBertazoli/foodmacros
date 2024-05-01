from js.jquery import jquery
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import os
from dotenv import load_dotenv
from .models import Add_Food
from .forms import AddFoodForm
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


def account(request):
    return render(request, 'account/index.html')


def tracker(request):
    foods = Add_Food.objects.filter(user=request.user)
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
    foods = Add_Food.objects.filter(user=request.user)
    print(data)
    return render(request, 'account/tracker.html', {'data': data, 'foods': foods})


class FoodCreate(CreateView):
    model = Add_Food
    fields = ['name', 'weight', 'calories',
              'protein', 'fat', 'carbs', 'meal', 'date']
    success_url = '/account/tracker'
    # foods = Add_Food.objects.all()
    # if CreateView == 'POST':
    #     form = AddFoodForm(CreateView.POST)
    # calories = float(CreateView.POST['calories'])
    # weight = float(CreateView.POST['weight'])
    # total = (calories*weight)/100
    # print(total)

    # request.POST['calories'] = total
    # print('weight', form.weight)
    # print('here', form.is_valid(), form.errors)
    # if form.is_valid():
    #     form.save()
    # success_url = render(
    #     CreateView, 'account/tracker.html', {'foods': foods})

    def for_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/account/tracker.html')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

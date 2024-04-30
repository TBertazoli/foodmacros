from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('account/tracker', views.tracker, name='tracker'),
    path('account/tracker/food', views.search, name='search'),
    path('account/tracker/create', views.food_create, name='food_create'),
]

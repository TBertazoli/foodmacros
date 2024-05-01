from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('account/tracker', views.tracker, name='tracker'),
    path('account/tracker/food', views.search, name='search'),
    path('account/tracker/create', views.FoodCreate.as_view(), name='food_create'),
    path('account/tracker/<int:pk>/delete/',
         views.FoodDelete.as_view(), name='food_delete'),
    path('account/tracker/<int:pk>/update/',
         views.FoodUpdate.as_view(), name='food_update'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup, name='signup')
]

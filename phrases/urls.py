from django.urls import path
from . import views

app_name = 'phrases'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('get-phrase/', views.get_phrase, name='get_phrase'),
] 
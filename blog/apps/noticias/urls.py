from django.urls import path
from . import views

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [

    path('', views.inicio, name="inicio"),

]

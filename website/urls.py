from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name="home.html"),
    path('how.html', views.how, name='how.html'),
    path('about.html', views.about, name='about.html')
]

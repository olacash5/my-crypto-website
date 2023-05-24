from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name="sign_up"),
    path('login', views.login, name="login"),
    path('wallet', views.wallet, name="wallet"),
    path('logout', views.logout, name="logout")
]
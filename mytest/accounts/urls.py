from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', LoginView.as_view(template_name='accounts/logout.html'))
]

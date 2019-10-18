from django.contrib import admin
from django.urls import path, include
from mytest import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

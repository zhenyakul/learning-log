"""определение схемы url для пользователей"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #включить url авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    #страница регистрации
    path('register/', views.register, name='register'),
]
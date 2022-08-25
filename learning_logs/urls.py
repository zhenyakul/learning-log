"""Определение схемы URL для learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #домашняя страница
    path('', views.index, name='index'),
    #страница с темами
    path('topics/', views.topics, name='topics'),
    #страницы с информацией в теме
    path('topics/<int:topic_id>', views.topicc, name='topic'),
    #страница для создание новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    #страница для создание новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #страница для редактирования записей
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
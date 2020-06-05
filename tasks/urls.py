from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getTask,name="home"),
    path('add_task/',views.AddTask,name="add_task"),
    path('delete_task/<int:id>/',views.DeleteTask,name="delete_task"),
    path('update_task/<int:id>/',views.UpdateCurrentTask,name ="update_task"),
]

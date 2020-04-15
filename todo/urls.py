from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='todo_list' ),
    path('form/',views.form,name='todo_form'),
]
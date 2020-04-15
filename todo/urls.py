from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='todo_list' ),
    path('form/',views.form,name='todo_form'),
    path('<int:id>/', views.form,name='todo_update' ),
      path('delete/<int:id>/', views.todo_del,name='todo_delete' ),
]
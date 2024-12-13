from django.urls import path # type: ignore
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_task/', views.view_task, name='view_task'),
    path('suggestions/', views.suggestions, name='suggestions'),
]
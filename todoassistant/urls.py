"""
URL configuration for todoassistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_task/', views.view_task, name='view_task'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('view-task/', views.view_task, name='view_task'),
    path('get-all-tasks/', views.get_all_tasks, name='get_all_tasks'),
    path('search-task/', views.search_task, name='search_task'),
]

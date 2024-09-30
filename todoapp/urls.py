"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("registration/",views.SignupView.as_view(),name="signup"),

    path("",views.LoginView.as_view(),name="login"),

    path("logout",views.LogoutView.as_view(),name="logout"),

    path("todocreate/",views.TodoCreateView.as_view(),name="todo-create"),

    path("todotable/",views.TodolistView.as_view(),name="todo-list"),

    path("todo/<int:pk>/update",views.TodoupdateView.as_view(),name="todo-update"),

    path("todo/<int:pk>/completed/",views.TodocompleteView.as_view(),name="todo-completed"),

    path("todo/<int:pk>/delete",views.TodoDeleteView.as_view(),name="todo-delete"),

    path("todo/personal",views.Todopersonalview.as_view(),name="todo-personal"),
    
    

    path("todo/work",views.Todoworkview.as_view(),name="todo-work"),

    path("todo/wishlist/",views.Todowishlistview.as_view(),name="todo-wishlist"),

    path("todo/shopping/",views.Todoshoppingview.as_view(),name="todo-shopping"),

    # path("todo/filter/",views.FilterbyDateView.as_view(),name="todo-filter")

    




]

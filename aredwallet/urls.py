"""
URL configuration for aredwallet project.

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
from django.contrib import admin
from django.urls import path
from .controllers import todo_controller, user_controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', todo_controller.todo_list),
    path('todos/<int:pk>/', todo_controller.todo_detail),
    path('todos/<int:pk>/delete/', todo_controller.delete_todo),
    path('todos/<int:pk>/update/', todo_controller.update_todo),
    path('users/', user_controller.user_list),
    path('users/<int:pk>/', user_controller.user_detail),
]


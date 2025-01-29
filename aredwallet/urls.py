from django.contrib import admin
from django.urls import path
from .controllers import todo_controller, user_controller
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', todo_controller.todo_list),
    path('todos/<int:pk>/', todo_controller.todo_detail),
    path('todos/<int:pk>/delete/', todo_controller.delete_todo),
    path('todos/<int:pk>/update/', todo_controller.update_todo),
    path('users/', user_controller.user_list),
    path('users/<int:pk>/', user_controller.user_detail),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


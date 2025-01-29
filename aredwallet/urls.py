from django.contrib import admin
from django.urls import path
from .controllers import todo_controller, user_controller
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .controllers.users_controller import UserView, RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', todo_controller.todo_list),
    path('todos/<int:pk>/', todo_controller.todo_detail),
    path('todos/<int:pk>/delete/', todo_controller.delete_todo),
    path('todos/<int:pk>/update/', todo_controller.update_todo),
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', user_controller.user_detail),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]


from django.urls import path
from .views import RegisterView, LoginView, GetProfileView, UpdateProfileView, DeleteProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/get_profile/', GetProfileView.as_view(), name='get_profile'),
    path('api/v1/update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('api/v1/delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
]

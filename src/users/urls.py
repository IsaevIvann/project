from django.urls import path
from .views import RegisterView, LoginView, GetProfileView, UpdateProfileView, DeleteProfileView, UploadUserPhotoView, \
    UploadUserPhotosView, CustomTokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('get_profile/', GetProfileView.as_view(), name='get_profile'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
    path('upload-photo/', UploadUserPhotoView.as_view(), name='upload-photo'),
    path('upload-photos/', UploadUserPhotosView.as_view(), name='upload_user_photos'),
]

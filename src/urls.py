from django.contrib import admin
from django.urls import path

# from src.users.views import UserApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/userlist/', UserApiView.as_view()),

]

admin.site.site_header = "Одмэнка"
admin.site.index_title = "Одmanка"
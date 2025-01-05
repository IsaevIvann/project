# from django.apps import AppConfig
#
#
# class UsersConfig(AppConfig):
#     verbose_name = "Все пользователи"
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'src.users'

from django.apps import AppConfig


class UsersConfig(AppConfig):
    verbose_name = "Пользователи"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.users'

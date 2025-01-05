from django.apps import AppConfig


class TechnicalConfig(AppConfig):
    verbose_name = "Технический раздел"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.technical'

from django.apps import AppConfig


class AvatarsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avatars'

    # Создание записей в БД при миграции
    def ready(self): from . import signals

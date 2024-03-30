from django.apps import AppConfig


class LogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'log_analysis'

    def ready(self):
        from .models import LogParsingRule
        LogParsingRule.load_from_config()

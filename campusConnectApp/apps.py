from django.apps import AppConfig


class CampusconnectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campusConnectApp'

    def ready(self):
        import campusConnectApp.signals
from django.apps import AppConfig


class CampusconnectappConfig(AppConfig):
    name = 'campusConnectApp'

    def ready(self):
        import campusConnectApp.signals

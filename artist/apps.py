from django.apps import AppConfig


class ArtistApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist'

    def ready(self):
        import artist.signals

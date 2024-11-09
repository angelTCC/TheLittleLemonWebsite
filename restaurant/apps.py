from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'

    # added

    verbose_name = 'Restaurant Management'  # Improves display name in admin

    def ready(self):
        print("Restaurant app is ready!")  # Print confirmation message
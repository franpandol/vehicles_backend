from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a superuser if there are no existing users"

    def handle(self, *args, **options):
        if not get_user_model().objects.exists():
            get_user_model().objects.create_superuser(username="admin", email="admin@admin.com", password="admin")
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.NOTICE("Superuser already exists"))

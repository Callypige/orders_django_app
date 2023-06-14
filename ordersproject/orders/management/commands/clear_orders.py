from django.core.management.base import BaseCommand
from orders.models import Order


class Command(BaseCommand):
    help = "Clears all data from the Order model"

    def handle(self, *args, **options):
        # Delete all Order objects
        Order.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS("All Order model data cleared.")
        )

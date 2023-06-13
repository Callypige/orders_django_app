from django.core.management.base import BaseCommand, CommandParser
from orders.models import Order
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    # Command help description
    help = "Imports order from XML file to the order model"

    def add_arguments(self, parser: CommandParser) -> None:
        # Add command-line argument for XML file path
        parser.add_argument("xml_file", type=str, help="Path to the XML file")

    def handle(self, *args, **options):
        # Retrieve the XML file path from command-line arguments
        xml_file_path = options.get("xml_file")

        try:
            # Parse the XML file
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
        except ET.ParseError:
            # Handle invalid XML file error
            self.stderr.write(self.style.ERROR("Invalid XML file."))
            return

        for order in root.findall("orders/order"):
            # Extract field values from the order element
            order_id = order.findtext("order_id")
            marketplace = order.findtext("marketplace")
            order_purchase_date = order.findtext("order_purchase_date")
            order_currency = order.findtext("order_currency")
            order_amount = order.findtext("order_amount")

            if None in (
                order_id,
                marketplace,
                order_purchase_date,
                order_currency,
                order_amount,
            ):
                # Handle missing elements error
                self.stderr.write(
                    self.style.ERROR("Some elements are missing in the XML.")
                )
                continue

            # Create or retrieve the Order object
            order_obj, created = Order.objects.get_or_create(
                order_id=order_id,
                defaults={
                    "marketplace": marketplace,
                    "order_purchase_date": order_purchase_date,
                    "order_currency": order_currency,
                    "order_amount": order_amount,
                },
            )

            if created:
                self.stdout.write(f"Order created: {order_obj}")
                # Indicate successful processing
                self.stdout.write(self.style.SUCCESS("Data saved."))
            else:
                self.stdout.write(
                    self.style.ERROR(f"Order already exists: {order_obj}")
                )

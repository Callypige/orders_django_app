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
        except Exception:
            # Handle invalid XML file error
            self.stderr.write(self.style.ERROR("Invalid XML file."))

        try:
            # Process each order element
            for order in root.findall("orders/order"):
                # Extract field values from the order element
                order_id = order.find("order_id").text
                marketplace = order.find("marketplace").text
                order_purchase_date = order.find("order_purchase_date").text
                order_currency = order.find("order_currency").text
                order_amount = order.find("order_amount").text

                # Now need to create an order object
                order = Order.objects.create(
                    order_id=order_id,
                    marketplace=marketplace,
                    order_purchase_date=order_purchase_date,
                    order_currency=order_currency,
                    order_amount=order_amount,
                )

                order.save()

                self.stdout.write(f"Order saved : {order}")

            # Indicate successful processing
            self.stdout.write(self.style.SUCCESS("Successfully saved data."))
        except Exception as e:
            # Handle invalid XML file error
            self.stderr.write(self.style.ERROR(f"Error : {e}"))

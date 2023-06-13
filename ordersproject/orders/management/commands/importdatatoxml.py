from django.core.management.base import BaseCommand, CommandParser
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = "Imports order from XML file to the order model"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("xml_file", type=str, help="Path to the XML file")

    def handle(self, *args, **options):
        xml_file_path = options.get("xml_file")
        try:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

            # count_total = int(tree.find("orders_count/count_total").text)

            for order in root.findall("orders/order"):
                order_id = order.find("order_id").text
                marketplace = order.find("marketplace").text
                order_purchase_date = order.find("order_purchase_date").text
                order_currency = order.find("order_currency").text
                order_amount = order.find("order_amount").text

                # Afficher les valeurs des champs
                print("order_id =", order_id)
                print("marketplace =", marketplace)
                print("order_purchase_date =", order_purchase_date)
                print("order_currency =", order_currency)
                print("order_amount =", order_amount)
                print()

            self.stdout.write(self.style.SUCCESS("Successfull"))
        except Exception:
            self.stderr.write(self.style.ERROR("Invalid XML file."))

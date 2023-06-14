from django.core.management import call_command
from django.test import TestCase
from io import StringIO
from orders.models import Order
import datetime


class ImportOrderCommandTestCase(TestCase):
    def test_import_order_command(self):
        # Préparer les données de test
        xml_file_path = "orders-test.xml"

        # Appeler la commande
        out = StringIO()
        call_command("importdatatoxml", xml_file_path, stdout=out)

        # Vérifier les résultats
        output = out.getvalue()
        self.assertIn("Data saved.", output)

        # Vérifier que les données ont été importées dans le modèle Order
        order_count = Order.objects.count()
        self.assertEqual(order_count, 5)


class ShowUrlsCommandTestCase(TestCase):
    def test_show_urls_command(self):
        # Call the command and capture the output
        out = StringIO()
        call_command("show_urls", stdout=out)
        output = out.getvalue()

        # Assert the expected URL is present in the output
        self.assertIn("^orders/", output)
        self.assertIn("orders/^(?P<order_id>", output)


class ClearOrdersCommandTestCase(TestCase):
    def setUp(self):
        # Create some sample Order objects
        Order.objects.create(
            order_id="123-4567890-1112131",
            marketplace="amazon",
            order_purchase_date=datetime.date(2014, 10, 20),
            order_currency="EUR",
            order_amount="115.50",
        )

    def test_clear_orders_command(self):
        # Call the command
        call_command("clear_orders")

        # Assert that all Order objects have been deleted
        order_count = Order.objects.count()
        self.assertEqual(order_count, 0)

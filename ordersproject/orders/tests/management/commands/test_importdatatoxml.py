from django.core.management import call_command
from django.test import TestCase
from io import StringIO
from orders.models import Order


class ImportOrderCommandTestCase(TestCase):
    def test_import_order_command(self):
        # Préparer les données de test
        xml_file_path = "chemin/vers/votre/fichier.xml"

        # Appeler la commande
        out = StringIO()
        call_command("import_orders", xml_file_path, stdout=out)

        # Vérifier les résultats
        output = out.getvalue()
        self.assertIn("Data saved.", output)

        # Vérifier que les données ont été importées dans le modèle Order
        order_count = Order.objects.count()
        self.assertEqual(order_count, 1)

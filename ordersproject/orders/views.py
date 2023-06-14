from django.http import JsonResponse
import json
from django.core.serializers import serialize
from orders.models import Order


def serialize_order_data(orders):
    serialized_orders = serialize("json", orders)
    formatted_json = json.loads(serialized_orders)
    return formatted_json


def order_list(request):
    # Get all orders
    orders = Order.objects.all()

    # Serialize orders into JSON
    formatted_json = serialize_order_data(orders)

    # Return the JSON response
    return JsonResponse(
        formatted_json,
        json_dumps_params={"indent": 4, "ensure_ascii": False},
        safe=False,
    )


def order_detail(request, order_id):
    try:
        # Get the order with the specified order_id
        order = Order.objects.get(order_id=order_id)

        # Serialize order into JSON
        formatted_json = serialize_order_data([order])

        # Return the JSON response
        return JsonResponse(
            formatted_json,
            json_dumps_params={"indent": 4, "ensure_ascii": False},
            safe=False,
        )
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

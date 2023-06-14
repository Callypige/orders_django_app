from django.http import JsonResponse
import json
from django.core.serializers import serialize
from orders.models import Order


def order_list(request):
    # get all orders
    orders = Order.objects.all()
    # Serialize orders into JSON
    serialized_orders = serialize("json", orders)
    formatted_json = json.loads(serialized_orders)

    # Return the JSON response
    return JsonResponse(
        formatted_json,
        json_dumps_params={"indent": 4, "ensure_ascii": False},
        safe=False,
    )


def order_detail(request, order_id):
    try:
        order = Order.objects.filter(order_id=order_id)
        serialized_orders = serialize("json", order)
        formatted_json = json.loads(serialized_orders)

        # Return the JSON response
        return JsonResponse(
            formatted_json,
            json_dumps_params={"indent": 4, "ensure_ascii": False},
            safe=False,
        )
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

import os
import django
from .models import Order
import dramatiq

from celery import shared_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

# @dramatiq.actor
# def process_order(order_id):
#     try:
#         order = Order.objects.get(id=order_id)
#         order.status = 'processed'
#         order.save()
#         return f"Order {order_id} processed"
#     except Order.DoesNotExist:
#         return f"Order {order_id} does not exist"


@shared_task
def process_order(order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = 'processed'
        order.save()
        return f"Order {order_id} processed"
    except Order.DoesNotExist:
        return f"Order {order_id} does not exist"



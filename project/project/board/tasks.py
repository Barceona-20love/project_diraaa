from celery import shared_task
from .models import Order
import time
@shared_task
def complete_order(oid):
    order = Order.objects.get(pk = oid)
    order.complete = True
    order.save()
def complete_order():
    return None
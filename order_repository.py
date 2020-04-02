from flask import json
from random import random

with open('orders.json', 'r+') as shops_file:
    data = json.load(shops_file)


def find_orders():
    return data


def find_order(order_id):

    for order in data['orders']:
        if str(order['id']) == str(order_id):
            return order

    return None


def create_order(order):

    order_to_create = {
        "id": round(random() * 100000),
        "shop": order['shop'],
        "product": order['product'],
        "q": order['q'],
        "amount": order['amount'],
        "totalAmount": order['q'] * order['amount']
    }

    data['orders'].append(order_to_create)
    return data


def delete_order(order_id):

    order = find_order(order_id)

    if not order:
        return None

    data['orders'].remove(order)

    return order


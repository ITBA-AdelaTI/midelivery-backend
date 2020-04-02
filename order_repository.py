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


def update_order(order_id, new_order):

    old_order = find_order(order_id)

    if not old_order:
        return None

    order_to_update = {
        "id": old_order['id'],
        "shop": new_order['shop'],
        "product": new_order['product'],
        "q": new_order['q'],
        "amount": new_order['amount'],
        "totalAmount": new_order['amount'] * new_order['q'],
    }

    old_index = data['orders'].index(old_order)

    data['orders'][old_index] = order_to_update

    return order_to_update


def delete_order(order_id):

    order = find_order(order_id)

    if not order:
        return None

    data['orders'].remove(order)

    return order


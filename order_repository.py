from random import random
from utils import get_db
from bson.json_util import dumps

collection = get_db().orders


def find_orders():
    orders = collection.find({}, {'_id': 0})
    return dumps(orders)


def find_order(order_id):

    order = collection.find_one({'id': int(order_id)}, {'_id': 0})

    print(order)

    if not order:
        return None

    return dumps(order)


def create_order(order):
    order_to_create = {
        "id": round(random() * 100000),
        "shop": order['shop'],
        "product": order['product'],
        "q": order['q'],
        "amount": order['amount'],
        "totalAmount": order['q'] * order['amount']
    }

    inserted_id = collection.insert_one(order_to_create).inserted_id
    return dumps(inserted_id)


def update_order(order_id, new_order):

    result = collection.update_one({'id': int(order_id)},
                                   {'$set': {
                                       'shop': new_order['shop'],
                                       "product": new_order['product'],
                                       "q": new_order['q'],
                                       "amount": new_order['amount'],
                                       "totalAmount": new_order['amount'] * new_order['q']
                                   }
                                   })

    return find_order(order_id) if result.modified_count == 1 else None


def delete_order(order_id):

    order_to_delete = find_order(order_id)

    result = collection.delete_one({'id': int(order_id)})

    return order_to_delete if result.deleted_count == 1 else None

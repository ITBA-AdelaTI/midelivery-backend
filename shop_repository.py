from utils import get_db
from bson.json_util import dumps


collection = get_db().shops


def find_shops():
    shops = collection.find({}, {'_id': 0})
    return dumps(shops)


def find_shop(shop_id):

    shop = collection.find_one({'id': int(shop_id)}, {'_id': 0})

    print(shop)

    if not shop:
        return None

    return dumps(shop)


def find_products(shop_id):

    shop = collection.find_one({'id': int(shop_id)})

    return dumps(shop['products']) if shop else []


def find_product(shop_id, product_id):

    product = collection.find({'id': int(shop_id)},
                              {'products': {'$elemMatch': {'sku': int(product_id)}}, "_id": 0})

    print(product)

    return dumps(product)


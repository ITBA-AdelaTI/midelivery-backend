from flask import json

with open('shops.json', 'r') as shops_file:
    data = json.load(shops_file)


def find_shops():
    return data


def find_shop(shop_id):

    for shop in data['shops']:
        if str(shop['id']) == str(shop_id):
            return shop

    return None


def find_products(shop_id):

    for shop in data['shops']:
        if str(shop['id']) == str(shop_id):
            return shop['products']

    return []


def find_product(shop_id, product_id):

    products = find_products(shop_id)

    if not products:
        return None

    for prod in products:
        if str(prod['sku']) == str(product_id):
            return prod

    return None


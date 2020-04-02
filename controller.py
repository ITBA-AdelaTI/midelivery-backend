from flask import Flask, request
from flask_cors import CORS
from shop_repository import *
from order_repository import *

app = Flask(__name__)
CORS(app)

# Shops


@app.route('/shops', methods=['GET'])
def get_shops():

    shops = find_shops()

    if not shops:
        return '[]', 404

    return shops, 200


@app.route('/shops/<id_shop>', methods=['GET'])
def get_shop(id_shop):

    shop = find_shop(id_shop)

    if not shop:
        return {"error": "Shop not found"}, 404

    return shop, 200


@app.route('/shops/<id_shop>/products', methods=['GET'])
def get_shop_products(id_shop):

    products = find_products(id_shop)

    if not products:
        return '[]', 404

    return json.dumps(products), 200


@app.route('/shops/<shop_id>/products/<product_id>', methods=['GET'])
def get_shop_product(shop_id, product_id):

    product = find_product(shop_id, product_id)

    if not product:
        return {"error": "Product not found"}, 404

    return product, 200

# Orders


@app.route('/orders', methods=['GET'])
def get_orders():

    orders = find_orders()

    if not orders:
        return '[]', 404

    return orders, 200


@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):

    order = find_order(order_id)

    if not order:
        return {"error": "Order not found"}, 404

    return order, 200


@app.route('/orders', methods=['POST'])
def add_order():

    created = create_order(request.json)

    return created, 201


@app.route('/orders/<order_id>', methods=['DELETE'])
def remove_order(order_id):

    deleted = delete_order(order_id)

    if not deleted:
        return {"error": "Order not found to be deleted"}, 404

    return deleted, 200

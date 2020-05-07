from flask import Flask, request, Response, jsonify
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

    return Response(response=shops, status=200, mimetype="application/json")


@app.route('/shops/<id_shop>', methods=['GET'])
def get_shop(id_shop):

    shop = find_shop(id_shop)

    if not shop:
        return {"error": "Shop not found"}, 404

    return Response(response=shop, status=200, mimetype="application/json")


@app.route('/shops/<id_shop>/products', methods=['GET'])
def get_shop_products(id_shop):

    products = find_products(id_shop)

    if not products:
        return '[]', 404

    return Response(response=products, status=200, mimetype="application/json")


@app.route('/shops/<shop_id>/products/<product_id>', methods=['GET'])
def get_shop_product(shop_id, product_id):

    product = find_product(shop_id, product_id)

    if not product:
        return {"error": "Product not found"}, 404

    return Response(response=product, status=200, mimetype="application/json")


# Orders


@app.route('/orders', methods=['GET'])
def get_orders():

    orders = find_orders()

    if not orders:
        return '[]', 404

    return Response(response=orders, status=200, mimetype="application/json")


@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):

    order = find_order(order_id)

    if not order:
        return {"error": "Order not found"}, 404

    return Response(response=order, status=200, mimetype="application/json")


@app.route('/orders', methods=['POST'])
def add_order():

    created_id = create_order(request.json)

    return Response(response=created_id, status=201, mimetype="application/json")


@app.route('/orders/<order_id>', methods=['PUT'])
def edit_order(order_id):

    edited_order = update_order(order_id, request.json)

    if not edited_order:
        return {"error": "Order not found to be edited"}, 404

    return Response(response=edited_order, status=200, mimetype="application/json")


@app.route('/orders/<order_id>', methods=['DELETE'])
def remove_order(order_id):

    deleted = delete_order(order_id)

    if not deleted:
        return {"error": "Order not found to be deleted"}, 404

    return Response(response=deleted, status=200, mimetype="application/json")

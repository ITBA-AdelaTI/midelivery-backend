from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/shops')
def get_products():

    with open('shops.json', 'r+') as f:
        data = json.load(f)

    return data, 200


@app.route('/shops/<id_shop>')
def get_product(id_shop):

    with open('shops.json', 'r+') as f:
        data = json.load(f)

    for product in data['products']:
        if str(product['id']) == str(id_shop):
            return product, 200

    return '{"Error": "Shop not found" }', 404


@app.route('/products', methods=['POST'])
def create_product():
    with open('shops.json', 'r+') as file:
        data = json.load(file)

    data['products'].append(request.json)

    return data, 201

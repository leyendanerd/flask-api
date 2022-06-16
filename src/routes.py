from crypt import methods
from flask import jsonify, Blueprint, request
from products import products


api = Blueprint('api', __name__)


@api.route('/ping')
def ping():
    return jsonify({"messages": 'pong'})


@api.route('/products')
def getProducts():
    return jsonify({"products": products, "messages": "product list"})


@api.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product encontrado": productsFound[0]})

    return jsonify({"messages": "Producto no encontrado"})


@api.route('/products', methods=['POST'])
def addProducts():
    new_product = {
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity": request.json['quantity']

    }

    products.append(new_product)
    return jsonify({"messages": "Producto agregado", "Products": products})

@api.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})
    

@api.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })
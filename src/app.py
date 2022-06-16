from flask import Flask, jsonify
from products import products
from routes import api

app= Flask(__name__)

app.register_blueprint(api)

if __name__=='__main__':
    app.run(debug=True)



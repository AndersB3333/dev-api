from flask import Flask, jsonify, request, jsonify
from flask_restful import Resource, Api

import numpy as np
import pandas as pd
import random as random

app = Flask(__name__)
api = Api(app)

class Hand(Resource):
    def post(self):
        request_data = request.get_json()
        request_data.headers.add('Access-Control-Allow-Origin', '*')
        return request_data


api.add_resource(Hand, '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, make_response, request
from flask_restful import Api, Resource
import json
import random

app = Flask(__name__)
api = Api(app)


class Britney(Resource):
    def get(self):
        with open('quotes.json') as data_file:
            quotes = json.load(data_file)
            random_quote = random.choice(quotes)
            if request.args.get("format") == "text":
                response = make_response(random_quote, 200)
                response.mimetype = "text/plain"
                return response
            return random_quote, 200


api.add_resource(Britney, '/')
if __name__ == '__main__':
    app.run(debug=True)
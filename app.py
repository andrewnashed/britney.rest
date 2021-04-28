from flask import Flask, make_response, request
from flask_restful import Api, Resource
import requests
import json
import random

app = Flask(__name__)
api = Api(app)


class Britney(Resource):
    def get(self):
        url = "https://raw.githubusercontent.com/andrewnashed/britney.rest/main/quotes.json"
        response = requests.get(url)
        quotes = json.loads(response.content.decode())
        random_quote = random.choice(quotes)
        if request.args.get("format") == "text":
            response = make_response(random_quote, 200)
            response.mimetype = "text/plain"
            return response
        return random_quote, 200


api.add_resource(Britney, '/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
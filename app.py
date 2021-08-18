from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


class get_all_articles(Resource):
    def get(self, keyword='Space'):
        api_url = 'https://api.spaceflightnewsapi.net/v3/articles'
        response = requests.get(api_url)
        responses = response.json()

        articles = list()
        for article in responses:
            if keyword in article['title']:
                articles.append(article['title'])

        return articles


api.add_resource(get_all_articles, '/')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
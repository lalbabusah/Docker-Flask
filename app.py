from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from elasticsearch import Elasticsearch
import requests
import json


app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def store_record():
    url = 'https://api.spaceflightnewsapi.net/v3/articles'
    response = requests.get(url)
    responses = response.json()
    for response in responses:
        es.index(index='myindex', doc_type='article', id=response['id'], body=response)
    return None


@app.route('/search', methods=['GET'])
def article_search():
    keyword = 'Space' #request.args.get('keyword')
    keyword_search = json.dumps({'query': {'match': {'title': keyword}}})
    resources = es.search(index='myindex', body=keyword_search)

    articles = list()
    for article in resources['hits']['hits']:
        articles.append(article['_source']['title'])
    print(articles)
    return articles


if __name__ == '__main__':
    store_record()
    article_search()
    #app.run(host='0.0.0.0', port=5000)

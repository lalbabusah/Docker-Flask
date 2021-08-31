from flask import Flask, request, jsonify, json
from connect_elasticsearch import ConnectElasticsearch
from store_record import StoreRecord


app = Flask(__name__)


@app.route('/search', methods=['GET'])
def article_search():
    keyword = request.args.get("keyword")
    try:
        keyword_search = json.dumps({'query': {'match': {'title': keyword}}})
        resources = es.search(index='index', body=keyword_search)

        articles = list()
        for article in resources['hits']['hits']:
            articles.append(article['_source']['title'])

        response = jsonify(articles=articles), 200

    except:
        response = jsonify(message='Some Error Occurred'), 404

    finally:
        return response


if __name__ == '__main__':
    global es
    es = ConnectElasticsearch('localhost', 9200).connect()
    url = 'https://api.spaceflightnewsapi.net/v3/articles'
    StoreRecord(url, es).store()
    app.run(host='0.0.0.0', port=5000)


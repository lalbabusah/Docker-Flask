from elasticsearch import Elasticsearch, ElasticsearchException
from requests import get, RequestException


class StoreRecord:
    def __init__(self, url, es):
        self.url = url
        self.es = es

    def store(self):
        try:
            responses = get(self.url)
            for response in responses.json():
                self.es.index(index='index', doc_type='article', id=response['id'], body=response)
            print('Data stored!')

        except RequestException as Error:
            print(Error)

        except ElasticsearchException as Error:
            print(Error)
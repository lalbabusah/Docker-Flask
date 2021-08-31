from elasticsearch import Elasticsearch, ElasticsearchException


class ConnectElasticsearch:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        es = Elasticsearch([{'host': self.host, 'port': self.port}])
        if es.ping():
            print('Elasticsearch Connected!')
            return es
        else:
            raise ValueError('Connection Failed!')

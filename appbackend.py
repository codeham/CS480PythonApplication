import requests
from elasticsearch import Elasticsearch
import json

# global index
index = 0
# establish connection object
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

r = requests.get('http://localhost:9200')

def formatprint(jsonobj):
    print json.dumps(jsonobj, indent=2)

def increment():
    global index
    index += 1
    return index

def jsontodb(jsonobj):
    es.index(index='elements', doc_type='logs', id=index, body=jsonobj)
    increment()

def getData():
    # get test, this is just getting back a document from the db
    formatprint(es.get(index='elements', doc_type='logs', id=0))
    formatprint(es.get(index='elements', doc_type='logs', id=400))
    formatprint(es.get(index='elements', doc_type='logs', id=20))
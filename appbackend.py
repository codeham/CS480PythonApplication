import requests
from elasticsearch import Elasticsearch
import json

# global index
index = 0
# establish connection object
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

r = requests.get('http://localhost:9200')

def printtest():
    return 'hello world'

def jsontodb(jsonobj):
    es.index(index='elements', doc_type='logs', id=index, body=jsonobj)
    global index
    index += 1
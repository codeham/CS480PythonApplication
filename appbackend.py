import requests
from elasticsearch import Elasticsearch
import json

# global index
index = 0
# establish connection object
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

r = requests.get('http://localhost:9200')

# simeple function that prints json objects with clarity
def formatprint(jsonobj):
    print json.dumps(jsonobj, indent=2)

# increment method returns global index to map database index (id = index)
def increment():
    global index
    index += 1
    return index

# maps schema to elasticsearch database from json file 'mapping.json'
def defineMapping():
    print 'this is where we define mapping'
    url = 'http://localhost:9200/testmapping/'
    payload = json.load(open("mapping.json"))
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

# takes in json object containing entry (ip, port, ...) & dumps it into DB
def jsontodb(jsonobj):
    es.index(index='elements', doc_type='logs', id=index, body=jsonobj)
    increment()

# searches db by key fied (key argument) & value (term argument)
# SETUP FOR TESTING
def search(key, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                key: term
            }
        }
    })
    response = es.search(index='elements', body=query)
    print formatprint(response)

# gets a document back from the data
# SETUP FOR TESTING
def getData():
    #get test, this is just getting back a document from the db
    formatprint(es.get(index='elements', doc_type='logs', id=0))
    formatprint(es.get(index='elements', doc_type='logs', id=400))
    formatprint(es.get(index='elements', doc_type='logs', id=20))

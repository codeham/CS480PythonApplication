import requests
import elasticsearch as es
import json

# global index
index = 0
# establish connection object
client = es.Elasticsearch([{'host': 'localhost', 'port': '9200'}])

r = requests.get('http://localhost:9200')

# simeple function that prints json objects with clarity
def formatprint(jsonobj):
    print json.dumps(jsonobj, indent=2)

# increment method returns global index to map database index (id = index)
def increment():
    global index
    index += 1
    return index

# creates new index along with proper schema for index
# loads schema settings from json file 'mapping.json'
def createIndex():
    payload_dict = json.load(open("mapping.json"))
    body = {'mappings': payload_dict}
    print payload_dict

    try:
        client.indices.create(index='mappings', body=body)
    except es.exceptions.TransportError as e:
        if e.error != 'index_already_exists_exception':
            raise

# takes in json object containing entry (ip, port, ...) & dumps it into DB
def jsontodb(jsonobj):
    client.index(index='mappings', doc_type='post', id=index, body=jsonobj)
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

# BELOW ARE THE CURRENT QUERIES I AM TESTING
# SETUP FOR TESTING
def getData():
    # formatprint(es.get(index='mappings', doc_type='post', id=0))
    body = json.load(open('es_query.json'))
    # this query below returns back the most used destination ports followed by printing the content..
    # to the terminal
    res = client.search(index='mappings', doc_type='post', body=body)

    print formatprint(res)

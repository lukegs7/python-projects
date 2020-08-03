import requests
import json
import pickle
import codecs

def test_req():
    url = "http://localhost:8000/api/detector/"
    model_document = {'name': 'geshuai', 'age': 12}
    model_document = codecs.encode(pickle.dumps(model_document),'base64').decode()
    data = {
        "name": "constant-detector",
        "model_document": model_document
    }
    res = requests.post(url, json=data, headers={'content-type': 'application/json'})
    md=json.loads(res.content)['model_document']
    unpicked=pickle.loads(codecs.decode(md.encode(),"base64"))
    print(unpicked)

def test_1():
    url = "http://localhost:8000/api/detector/"
    model_document = {'name': 'geshuai', 'age': 12}
    model_document=pickle.dumps(model_document,0)
    data = {
        "name": "constant-detector",
        "model_document": model_document.decode()
    }
    res = requests.post(url, json=data, headers={'content-type': 'application/json'})
    md = json.loads(res.content)['model_document']
    unpicked=pickle.loads(md.encode())
    print(unpicked)

# pickled = codecs.encode(pickle.dumps(obj), "base64").decode()
# unpickled = pickle.loads(codecs.decode(pickled.encode(), "base64"))



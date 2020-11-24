from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

db = mongo.db.products

def serialize(documents):
  result = []
  for document in documents:
    document['_id'] = str(document['_id'])
    result.append(document)
  return result

@app.route('/product/new', methods=['POST'])
def add_product():
  id = request.json['id']
  name = request.json['name']
  description = request.json['description']
  parameters =  request.json['parameters']
  req_data = request.get_json()
  db.insert_one(req_data).inserted_id
  return ('', 204)

@app.route('/product/find_by_param', methods=['GET'])
def find_product_by_param():
  key = request.json['key']
  value = request.json['value']
  documents = db.find({ 'parameters': { '$elemMatch': { 'key': key, 'value' : value } } } )
  return (jsonify(serialize(documents)))

@app.route('/product/find_by_id', methods=['GET'])
def find_product_by_id():
  id = request.json['id']
  documents = db.find({ 'id': id } )
  return (jsonify(serialize(documents)))

@app.route('/product/find_by_name', methods=['GET'])
def find_product_by_name():
  name = request.json['name']
  documents = db.find({ 'name': {"$regex": name}})
  return (jsonify(serialize(documents)))

@app.route('/product/find_all', methods=['GET'])
def find_product_all():
  documents = db.find()
  return (jsonify(serialize(documents)))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from store_db import *

app = Flask(__name__)

@app.route('/display')
def display():
    result = select()
    return jsonify({"Result" :result})

@app.route('/insert_store', methods = ['POST'])
def insertdata_store():
    data = request.get_json()
    insert_store(data['store_id'],data['store_name'])
    return jsonify({"message" : "Values inserted"})

@app.route('/insert_item', methods = ['POST'])
def insertdata_item():
    data = request.get_json()
    insert_item(data['item_id'],data['item_name'],data['item_value'])
    return jsonify({"message" : "Values inserted"})


@app.route('/search', methods = ['POST'])
def searchdata():
    data = request.get_json()
    result = search(data['store_name'])
    if len(result)>0:
        return jsonify({"message":"Result found"},{"result":result})
    else:
        return jsonify({"message":"No data"})

@app.route('/update_store', methods = ['POST'])
def updatedata_store():
    data = request.get_json()
    update_store(data['store_name'],data['store_id'])
    return jsonify({"message" : "Updated store"})

@app.route('/update_item', methods = ['POST'])
def updatedata_item():
    data = request.get_json()
    update_item(data['item_id'],data['item_name'],data['item_value'])
    return jsonify({"message" : "Updated item"})


app.run(port = 6061)
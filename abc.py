from flask import Flask, render_template, request, jsonify
import pymongo
import pandas as pd
app= app = Flask(__name__)
@app.route('/mangos',methods=['GET', 'POST'])
def func_insert():
    if request.method=='POST':
        db1=request.json['db1']
        col1=request.json['col1']
        dict1=request.json['dict1']
    client = pymongo.MongoClient("mongodb+srv://test:test@test.uh0wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db=client[db1]
    col=db[col1]
    col.insert_one(dict1)
    result="inserted successfully"
    return jsonify(result)
@app.route('/dels',methods=['POST'])
def dels():
    if request.method=='POST':
        db1 = request.json['db1']
        col1 = request.json['col1']
        dict1 = request.json['dict1']
    client = pymongo.MongoClient("mongodb+srv://test:test@test.uh0wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client[db1]
    col = db[col1]
    col.delete_one(dict1)
    return jsonify("Deleted successfully from the collection")

@app.route('/create',methods=['POST'])
def creation():
    if request.method=='POST':
        db1 = request.json['db1']
        col1 = request.json['col1']
    client = pymongo.MongoClient("mongodb+srv://test:test@test.uh0wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client[db1]
    col = db[col1]
    dict1={}
    col.insert_one(dict1)
    return jsonify("created collection successfully")
@app.route('/insert_many',methods=['POST'])
def inserts_many():
    if request.method=='POST':
        client_link =request.json['client_link']
        db1 = request.json['db1']
        col1 = request.json['col1']
        data_link=request.json['data_link']
    df = pd.read_csv(data_link)
    data = df.to_dict('records')
    client=pymongo.MongoClient(client_link)
    db = client[db1]
    col=db[col1]
    col.insert_many(data)
    return jsonify("bulk data inserted successfully")
@app.route('/find_and_update',methods=['POST'])
def find_update():
    if request.method == 'POST':
        client_link = request.json['client_link']
        db1 = request.json['db1']
        col1 = request.json['col1']
        find=request.json['find']
        update=request.json['update']
    client = pymongo.MongoClient(client_link)
    db = client[db1]
    col = db[col1]
    col.find_one_and_update(find,update)
    return jsonify("update the records")
@app.route('/find_the_record',methods=['POST'])
def find_the_record():
    if request.method=='POST':
        client_link = request.json['client_link']
        db1 = request.json['db1']
        col1 = request.json['col1']
        find = request.json['find']
    client = pymongo.MongoClient(client_link)
    db = client[db1]
    col = db[col1]
    d=col.find_one(find)
    return jsonify(str(d))
















if __name__ == '__main__':
    app.run()


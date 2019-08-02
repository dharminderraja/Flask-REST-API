from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import sys

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mydb'
app.config['MONGO_URI'] = 'mongodb+srv://testuser:e1nQUH8XmtKXGfzV@cluster0-tojlt.mongodb.net/mydb?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/list', methods=['GET'])
def get_list():
    _employees = mongo.db.employees

    if 'offset' not in request.args:
        offset = 0
    else :
        offset = int(request.args['offset'])

    if 'limit' not in request.args:
        limit = 5
    else :
        limit = int(request.args['limit'])

    if 'first_name' not in request.args:
        first_name = ""
    else :
        first_name = request.args['first_name']

    if 'last_name' not in request.args:
        last_name = ""
    else :
        last_name = request.args['last_name']
    
    if 'birth_date' not in request.args:
        birth_date = ""
    else :
        birth_date = request.args['birth_date']
    
    if 'address' not in request.args:
        address = ""
    else :
        address = request.args['address']

    if 'boss' not in request.args:
        boss = ""
    else :
        boss = request.args['boss']

    if 'salarylessthan' not in request.args:
        salarylessthan = sys.maxsize
    else :
        salarylessthan = int(request.args['salarylessthan'])

    if 'salarygreaterthan' not in request.args:
        salarygreaterthan = 0
    else :
        salarygreaterthan = int(request.args['salarygreaterthan'])

    starting_id = _employees.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']

    employees = _employees.find(
        {
            '$and':[
                {'_id': {'$gte': last_id}},
                {'first_name': {'$regex': first_name}},
                {'last_name': {'$regex': last_name}},
                {'birth_date': {'$regex': birth_date}},
                {'address': {'$regex': address}},
                {'boss': {'$regex': boss}},
                {'salary': {'$gt': salarygreaterthan}},
                {'salary': {'$lt': salarylessthan}},
            ]
        }
    ).sort('_id', pymongo.ASCENDING).limit(limit)

    output = []

    for employee in employees:
        output.append({'_id' : str(employee['_id']),'first_name' : employee['first_name'], 'last_name' : employee['last_name'], 
        'birth_date' : employee['birth_date'],'address' : employee['address'], 'boss' : employee['boss'],
        'salary' : employee['salary']})

    if offset + limit < _employees.count():
        next_url = '/list?limit=' + str(limit) + '&offset=' + str(offset + limit) + '&first_name=' + str(first_name) + '&last_name=' + str(last_name) + '&birth_date=' + str(birth_date) + '&address=' + str(address) + '&boss=' + str(boss) + '&salarygreaterthan=' + str(salarygreaterthan) + '&salarylessthan=' + str(salarylessthan)
    else :
        next_url = ""
        
    if offset == 0 :
        prev_url = ""
    else :
        prev_url = '/list?limit=' + str(limit) + '&offset=' + str(offset - limit) + '&first_name=' + str(first_name) + '&last_name=' + str(last_name) + '&birth_date=' + str(birth_date) + '&address=' + str(address) + '&boss=' + str(boss) + '&salarygreaterthan=' + str(salarygreaterthan) + '&salarylessthan=' + str(salarylessthan)

    result = {'result' : output, 'prev_url' : prev_url, 'next_url' : next_url}

    return jsonify(result)


@app.route('/create', methods=['POST'])
def create_employee():
    employee = mongo.db.employees 

    if 'first_name' not in request.json:
        return "Values are Incorrect"

    if 'last_name' not in request.json:
        return "Values are Incorrect"

    if 'birth_date' not in request.json:
        return "Values are Incorrect"
    
    if 'address' not in request.json:
        return "Values are Incorrect"

    if 'boss' not in request.json:
        return "Values are Incorrect"

    if 'salary' not in request.json:
        return "Values are Incorrect"

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    birth_date = request.json['birth_date']
    address = request.json['address']
    boss = request.json['boss']
    salary = request.json['salary']

    employee_id = employee.insert({'first_name' : first_name, 'last_name' : last_name, 'birth_date' : birth_date,
    'address' : address, 'boss' : boss, 'salary' : salary})

    new_employee = employee.find_one({'_id' : employee_id})

    output = {'_id' : str(new_employee['_id']),'first_name' : new_employee['first_name'], 'last_name' : new_employee['last_name'], 
    'birth_date' : new_employee['birth_date'],'address' : new_employee['address'], 'boss' : new_employee['boss'],
     'salary' : new_employee['salary']}

    return jsonify({'result' : output})


@app.route('/employee/<userid>', methods=['GET'])
def get_employee(userid):
    employee = mongo.db.employees.find_one_or_404({"_id":  ObjectId(userid)})
    output = {'_id' : str(employee['_id']),'first_name' : employee['first_name'], 'last_name' : employee['last_name'], 
    'birth_date' : employee['birth_date'],'address' : employee['address'], 'boss' : employee['boss'],
     'salary' : employee['salary']}

    return jsonify({'result' : output})


@app.route('/delete/<userid>', methods=['DELETE'])
def delete_employee(userid):
    employee = mongo.db.employees.find_one_or_404({"_id":  ObjectId(userid)})
    output = mongo.db.employees.delete_one({'_id': ObjectId(userid)})
    return "Success Fully Deleted"


@app.route('/update/<userid>', methods=['POST'])
def update_employee(userid):
    employee = mongo.db.employees.find_one_or_404({"_id":  ObjectId(userid)})

    update = dict()

    if 'first_name' in request.json:
        update['first_name'] = request.json['first_name']

    if 'last_name' in request.json:
        update['last_name'] = request.json['last_name']

    if 'birth_date' in request.json:
        update['birth_date'] = request.json['birth_date']
    
    if 'address' in request.json:
        update['address'] = request.json['address']

    if 'boss' in request.json:
        update['boss'] = request.json['boss']

    if 'salary' in request.json:
        update['salary'] = request.json['salary']

    mongo.db.employees.update_one(
            {"_id": ObjectId(userid)},
            {
                "$set": update
            }
        )

    return "Success Fully Updated"
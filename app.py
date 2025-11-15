from flask import Flask,jsonify,request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

students = [
    {
        "id":1,
        "name":"Alice",
        "age":21
    }
]

@app.route('/students',methods=["GET"])
def student():
    return jsonify({'students':students})

@app.route('/add_student',methods=['POST'])
def add_student():
    data = request.json 
    students.append(data)
    return jsonify({'message':'student added successfully'})

@app.route('/update_student/<int:index>',methods=['PATCH'])
def update_student(index):
    data = request.json 
    students[index].update(data)
    return jsonify({'message':'student updated successfully'})

@app.route('/delete_student/<int:index>',methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({'message':'student updated successfully'})

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=4000)

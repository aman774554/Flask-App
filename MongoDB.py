#pip install flask-pymongo

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Update with your DB details

mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    mongo.db.users.insert_one(data)
    return jsonify({"message": "User added!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {"_id": 0}))  # Exclude _id from output
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

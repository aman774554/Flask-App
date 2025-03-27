https://chatgpt.com/c/67e43db5-ec48-800d-a437-35e5a9d7af79

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (Replace with your credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Create tables (Run this once)
with app.app_context():
    db.create_all()

# ----------------- CRUD APIs ----------------- #

# 1. Create User
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user": new_user.to_dict()}), 201

# 2. Get All Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# 3. Get User by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

# 4. Update User
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "User updated", "user": user.to_dict()}), 200

# 5. Delete User
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
--------------------------------------------------------------
user = User.query.filter_by(email="test@example.com").first()  # Simple filter
user = User.query.filter(User.email == "test@example.com").first()  # More flexible

filter_by() → Simpler syntax, only for equal (=) comparisons.
filter() → Supports complex conditions like <, >, !=, LIKE, IN, etc.

users = User.query.filter(User.name.ilike("%john%")).all()
users = User.query.filter(User.id.in_([1, 2, 3])).all()
from sqlalchemy import func
result = db.session.query(User.name, func.count(User.id)).group_by(User.name).all()
users = User.query.order_by(User.name.desc()).all()
result = db.session.query(User.name, Order.amount).outerjoin(Order, User.id == Order.user_id).all()
===========================

In Flask projects, most developers use Flask-SQLAlchemy because it simplifies database management and integrates well with Flask apps. 
It manages engine, session, and Base internally, making it easier to use than raw SQLAlchemy.

For larger applications or microservices, some projects use raw SQLAlchemy with create_engine() and declarative_base(), especially 
if they want more control over database sessions and connections.



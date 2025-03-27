https://chatgpt.com/c/67e43db5-ec48-800d-a437-35e5a9d7af79
https://chatgpt.com/share/67e54d5a-c184-800d-b3f3-8a54cac9a1f1

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from jsonschema import validate, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# JSON Schema for validation
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "email": {
            "type": "string",
            "format": "email",
            "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        }
    },
    "required": ["name", "email"],
    "additionalProperties": False
}

# Create User
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        validate(instance=data, schema=user_schema)
    except ValidationError as e:
        return jsonify({"error": e.message}), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

# Read Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

# Read Single User
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

# Update User
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    try:
        validate(instance=data, schema=user_schema)
    except ValidationError as e:
        return jsonify({"error": e.message}), 400

    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

# Delete User
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
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



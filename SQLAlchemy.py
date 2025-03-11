# Install Dependencies
pip install flask flask-sqlalchemy pymysql

# Create the Flask App
from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import re

// Flask App Initialization
app = Flask(__name__)

// MySQL Database Configuration (Modify with your credentials)
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/mydatabase"
engine = create_engine(DATABASE_URL)

// SQLAlchemy Session
Session = sessionmaker(bind=engine)
session = Session()

// SQLAlchemy Base Model
Base = declarative_base()

// Email Validation Function
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None
    
==============================
# Define the User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, CheckConstraint("age >= 18"), nullable=False)  # Age constraint

// Create the table in MySQL
Base.metadata.create_all(engine)

==============================
# Create User (POST)
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not name or not email or not age:
        return jsonify({"error": "All fields (name, email, age) are required"}), 400

    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    if age < 18:
        return jsonify({"error": "Age must be at least 18"}), 400

    new_user = User(name=name, email=email, age=age)

    try:
        session.add(new_user)
        session.commit()
        return jsonify({"message": "User added successfully!", "user": data}), 201
    except IntegrityError:
        session.rollback()
        return jsonify({"error": "Email already exists"}), 400
==============================
# Get All Users (GET)
@app.route("/users", methods=["GET"])
def get_users():
    users = session.query(User).all()
    if not users:
        return jsonify({"message": "No users found"}), 404

    user_list = [{"id": user.id, "name": user.name, "email": user.email, "age": user.age} for user in users]
    return jsonify(user_list), 200
==============================    
# Get a Single User by ID (GET)
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_data = {"id": user.id, "name": user.name, "email": user.email, "age": user.age}
    return jsonify(user_data), 200
==============================    
# Update a User (PUT)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    new_name = data.get("name")
    new_email = data.get("email")
    new_age = data.get("age")

    if new_email and not is_valid_email(new_email):
        return jsonify({"error": "Invalid email format"}), 400

    if new_age and new_age < 18:
        return jsonify({"error": "Age must be at least 18"}), 400

    if new_name:
        user.name = new_name
    if new_email:
        user.email = new_email
    if new_age:
        user.age = new_age

    try:
        session.commit()
        return jsonify({"message": "User updated successfully!"}), 200
    except IntegrityError:
        session.rollback()
        return jsonify({"error": "Email already exists"}), 400
==============================        
# Delete a User (DELETE)
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    session.delete(user)
    session.commit()
    return jsonify({"message": f"User {user_id} deleted successfully!"}), 200
==============================
# Run the Flask App
    if __name__ == "__main__":
    app.run(debug=True)



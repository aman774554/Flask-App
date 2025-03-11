## Install Dependencies
pip install sqlalchemy pymysql

## Connect to MySQL Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/mydatabase"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

// Base class for ORM models
Base = declarative_base()

# Define the User Table (Model)
from sqlalchemy import Column, Integer, String
========================
class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

// Create the table in MySQL
Base.metadata.create_all(engine)
print("Table created successfully!")
========================
# Add a New User
def add_user(name, email, age):
    new_user = User(name=name, email=email, age=age)
    session.add(new_user)
    session.commit()
    print(f"User {name} added successfully!")

// Example usage
add_user("Alice", "alice@example.com", 25)

# Read (Fetch) All Users
def get_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Age: {user.age}")

// Example usage
get_users()
========================
# Update a User

def update_user(user_id, new_name=None, new_email=None, new_age=None):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        if new_age:
            user.age = new_age
        session.commit()
        print(f"User {user_id} updated successfully!")
    else:
        print("User not found.")

// Example usage
update_user(1, new_name="Alice Cooper", new_age=26)
========================
# Delete a User
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted successfully!")
    else:
        print("User not found.")

// Example usage
delete_user(1)
========================
# Full Example Execution

# Add users
add_user("John Doe", "john@example.com", 30)
add_user("Jane Doe", "jane@example.com", 28)

# Get all users
get_users()

# Update user
update_user(2, new_name="Jane Smith", new_age=29)

# Delete user
delete_user(1)

# Get users after deletion
get_users()




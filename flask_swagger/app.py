from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# --- DATABASE CONFIG ---
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- SWAGGER CONFIG ---
swagger = Swagger(app)

# --- MODEL ---
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

# ---------------------------------------------------------
# CREATE EMPLOYEE
# ---------------------------------------------------------
@app.route("/employee", methods=["POST"])
def create_employee():
    """
    Create a New Employee
    ---
    tags:
      - Employee
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Employee
          required:
            - name
            - age
          properties:
            name:
              type: string
              example: "Ravi"
            age:
              type: integer
              example: 28
    responses:
      200:
        description: Employee created successfully
    """
    data = request.json
    emp = Employee(name=data["name"], age=data["age"])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee created", "id": emp.id})


# ---------------------------------------------------------
# GET ALL EMPLOYEES
# ---------------------------------------------------------
@app.route("/employee", methods=["GET"])
def get_employees():
    """
    Get All Employees
    ---
    tags:
      - Employee
    responses:
      200:
        description: List of all employees
    """
    employees = Employee.query.all()
    data = [{"id": e.id, "name": e.name, "age": e.age} for e in employees]
    return jsonify(data)


# ---------------------------------------------------------
# GET EMPLOYEE BY ID
# ---------------------------------------------------------
@app.route("/employee/<int:id>", methods=["GET"])
def get_employee(id):
    """
    Get Employee by ID
    ---
    tags:
      - Employee
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Employee details
    """
    emp = Employee.query.get_or_404(id)
    return jsonify({"id": emp.id, "name": emp.name, "age": emp.age})


# ---------------------------------------------------------
# UPDATE EMPLOYEE
# ---------------------------------------------------------
@app.route("/employee/<int:id>", methods=["PUT"])
def update_employee(id):
    """
    Update Employee
    ---
    tags:
      - Employee
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - name: body
        in: body
        required: true
        schema:
          id: EmployeeUpdate
          properties:
            name:
              type: string
              example: "Updated Name"
            age:
              type: integer
              example: 30
    responses:
      200:
        description: Employee updated successfully
    """
    emp = Employee.query.get_or_404(id)
    data = request.json

    emp.name = data.get("name", emp.name)
    emp.age = data.get("age", emp.age)

    db.session.commit()
    return jsonify({"message": "Employee updated"})


# ---------------------------------------------------------
# DELETE EMPLOYEE
# ---------------------------------------------------------
@app.route("/employee/<int:id>", methods=["DELETE"])
def delete_employee(id):
    """
    Delete Employee
    ---
    tags:
      - Employee
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Employee deleted successfully
    """
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"})


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------
if __name__ == "__main__":
    if not os.path.exists("employees.db"):
        with app.app_context():
            db.create_all()

    app.run(debug=True)

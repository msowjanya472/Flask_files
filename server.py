from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

employee_bp = Blueprint('employee_bp', __name__)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    department = db.Column(db.String(100), nullable = False)
    salary = db.Column(db.Float, nullable = False)

    def to_dict(self):
        return {
    
        "id": self.id,
        "name": self.name,
        "department": self.department,
        "salary": self.salary
        }
    
#with app.app_context():
#    db.create_all()

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()
    #print(data)
    name = data.get("name")
    department = data.get("department")
    salary = data.get("salary")
    if not all([name, department,salary]):
        return jsonify({"error": "missing fields"}),400
    
    new_emp = Employee(name=name, department=department, salary=salary)
    db.session.add(new_emp)
    db.session.commit()
    return jsonify(new_emp.to_dict()),  201

@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    all_data = Employee.query.all()
    #return jsonify({"a": all_data})    
    return jsonify([emp.to_dict() for emp in all_data])    

@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employees_id(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(emp.to_dict())    
    


@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employees(id):
    emp = Employee.query.get(id) 
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    data = request.get_json()  
    emp.name = data.get("name",emp.name)
    emp.department = data.get("department",emp.department)
    emp.salary = data.get("salary",emp.salary)
    db.session.commit()
    return jsonify(emp.to_dict()), 201
     
    


@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employees(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return '', 204

# Backwards-compatible shim: expose package-level objects
# Consumers can still `from app import create_app, db`.
from app import create_app, db  # type: ignore

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
   
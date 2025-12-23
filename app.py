from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:vinni%407116A@localhost:3306/b14_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
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

@app.route("/employees", methods=["POST"])
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

@app.route("/employees", methods=["GET"])
def get_employees():
    all_data = Employee.query.all()
    #return jsonify({"a": all_data})    
    return jsonify([emp.to_dict() for emp in all_data])    

@app.route("/employees/<int:id>", methods=["GET"])
def get_employees_id(id):
    emp = Employee.query.get(id)
    return jsonify(emp.to_dict())    
    


@app.route("/employees/<int:id>", methods=["PUT"])
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
     
    


@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employees(id):
    pass

if __name__ == "__main__":
    app.run(debug=True)
   
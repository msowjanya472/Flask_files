from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

# Package-level db and blueprint
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


@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()
    name = data.get("name")
    department = data.get("department")
    salary = data.get("salary")
    if not all([name, department, salary]):
        return jsonify({"error": "missing fields"}), 400

    new_emp = Employee(name=name, department=department, salary=salary)
    db.session.add(new_emp)
    db.session.commit()
    return jsonify(new_emp.to_dict()), 201


@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    all_data = Employee.query.all()
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
    emp.name = data.get("name", emp.name)
    emp.department = data.get("department", emp.department)
    emp.salary = data.get("salary", emp.salary)
    db.session.commit()
    return jsonify(emp.to_dict()), 201


@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employees(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return "", 204


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vinni%407116A@localhost:3306/b14_flask'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(employee_bp)
    with app.app_context():
        db.create_all()
    return app


# Maintain ability to run via `python -m app`
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

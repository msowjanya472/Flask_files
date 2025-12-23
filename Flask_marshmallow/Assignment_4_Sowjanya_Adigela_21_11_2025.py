#1. Implementation of Marshmellow Schema in Flask:
#--------------------------------------------------




#from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from marshmallow import Schema, fields
#from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
#
#app = Flask(__name__)
#
## MySQL Database Connection
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vinni%407116A@localhost:3306/b14_marshmallow'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = SQLAlchemy(app)
#
#
#class Employee(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    department = db.Column(db.String(100), nullable=False)
#    salary = db.Column(db.Float, nullable=False)
#
#
#
#class EmployeeSchema(SQLAlchemySchema):
#    class Meta:
#        model = Employee
#        load_instance = True
#
#    id = auto_field()
#    name = auto_field()
#    department = auto_field()
#    salary = auto_field()
#
#
#employee_schema = EmployeeSchema()
#employees_schema = EmployeeSchema(many=True)
#
#
##with app.app_context():
##    db.create_all()
#
#
#@app.route("/employees", methods=["POST"])
#def create_employee():
#    data = request.get_json()
#
#    new_emp = employee_schema.load(data, session=db.session)
#    db.session.add(new_emp)
#    db.session.commit()
#
#    return jsonify({"message": "Employee created", "employee": employee_schema.dump(new_emp)})
#
#
#
#@app.route("/employees", methods=["GET"])
#def get_employees():
#    all_data = Employee.query.all()
#    return jsonify(employees_schema.dump(all_data))
#
#
#
#@app.route("/employees/<int:id>", methods=["GET"])
#def get_employee_id(id):
#    emp = Employee.query.get(id)
##    return jsonify(emp.to_dict())
#
#
#
#@app.route("/employees/<int:id>", methods=["PUT"])
#def update_employee(id):
#    emp = Employee.query.get_or_404(id)
#    data = request.get_json()
#
#    emp.name = data.get("name", emp.name)
#    emp.department = data.get("department", emp.department)
#    emp.salary = data.get("salary", emp.salary)
#
#    db.session.commit()
#
#    return jsonify({"message": "Employee updated", "employee": employee_schema.dump(emp)})
#
#
#@app.route("/employees/<int:id>", methods=["DELETE"])
#def delete_employee(id):
#    emp = Employee.query.get_or_404(id)
#    db.session.delete(emp)
#    db.session.commit()
#
#    return jsonify({"message": "Employee deleted"})
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
#

#2) Implementation of  JWT Token in Flask:
#-----------------------------------------

#JWT TOKEN :

#from flask import Flask, jsonify, request
#from flask_jwt_extended import (
#    JWTManager, create_access_token,
#    jwt_required, get_jwt_identity
#)
#
#app = Flask(__name__)
#
## Secret key for JWT
#app.config["JWT_SECRET_KEY"] = "mysecret"  
#jwt = JWTManager(app)
#
## Dummy user
#USER = {
#    "username": "admin",
#    "password": "1234"
#}
#
#
#@app.route("/login", methods=["POST"])
#def login():
#    data = request.get_json()
#
#    if not data or data.get("username") != USER["username"] or data.get("password") != USER["password"]:
#        return jsonify({"message": "Invalid username or password"}), 401
#
#    # create token
#    access_token = create_access_token(identity=USER["username"])
#    return jsonify({
#        "message": "Login successful",
#        "token": access_token
#    })
#
#
#@app.route("/profile", methods=["GET"])
#@jwt_required()
#def profile():
#    current_user = get_jwt_identity()
#    return jsonify({
#        "message": "Access granted",
#        "logged_in_as": current_user
#    })
#
#
#
#@app.route("/")
#def index():
#    return jsonify({"message": "JWT Example Running"})
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
#

##3. Use MySQL as a DataBase in Flask:
#----------------------------------------


#from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
#
#app = Flask(__name__)
#
## -------------------------------------
## MySQL Database Configuration
## -------------------------------------
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:vinni%407116A@localhost/flask_demo"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#db = SQLAlchemy(app)
#
##
#class Student(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    marks = db.Column(db.Integer, nullable=False)
#
#    def to_dict(self):
#        return {"id": self.id, "name": self.name, "marks": self.marks}
#
##
##@app.before_request
##def create_tables():
##    db.create_all()
##

#@app.route("/student", methods=["POST"])
#def add_student():
#    data = request.get_json()
#    student = Student(name=data["name"], marks=data["marks"])
#    db.session.add(student)
#    db.session.commit()
#    return jsonify({"message": "Student added", "student": student.to_dict()})
#

#@app.route("/students", methods=["GET"])
#def get_students():
#    students = Student.query.all()
#    return jsonify([s.to_dict() for s in students])
#

#@app.route("/student/<int:id>", methods=["PUT"])
#def update_student(id):
#    student = Student.query.get_or_404(id)
#    data = request.get_json()
#    student.name = data["name"]
#    student.marks = data["marks"]
#    db.session.commit()
#    return jsonify({"message": "Student updated", "student": student.to_dict()})
#

#@app.route("/student/<int:id>", methods=["DELETE"])
#def delete_student(id):
#    student = Student.query.get_or_404(id)
#    db.session.delete(student)
#    db.session.commit()
#    return jsonify({"message": "Student deleted"})
#
#
#@app.route("/")
#def home():
#    return jsonify({"message": "Flask MySQL Example Running!"})
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
#

#4. Soft Delete  in Flask:
#------------------------


#
#
#Soft delete means:
#
# Do NOT remove a record from the database
# Instead mark it as “deleted”
#
#This is usually done by adding:
#
#is_deleted = db.Column(db.Boolean, default=False)
#
#
#
#
#from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
#
#app = Flask(__name__)
#
## Use SQLite for simplicity (You can replace with MySQL)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = SQLAlchemy(app)
#
#
##
#class Student(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50))
#    is_deleted = db.Column(db.Boolean, default=False)   # Soft delete flag
#
#
##
#with app.app_context():
#    db.create_all()
#

#@app.route("/student", methods=["POST"])
#def create_student():
#    data = request.json
#    student = Student(name=data["name"])
#    db.session.add(student)
#    db.session.commit()
#    return jsonify({"message": "Student created", "id": student.id})
#
#

#@app.route("/students", methods=["GET"])
#def get_students():
#    students = Student.query.filter_by(is_deleted=False).all()
#    result = [{"id": s.id, "name": s.name} for s in students]
#    return jsonify(result)
#
#
#
#@app.route("/student/<int:id>", methods=["DELETE"])
#def soft_delete_student(id):
#    student = Student.query.get(id)
#    if not student:
#        return jsonify({"message": "Student not found"})
#
#    student.is_deleted = True   # Mark as deleted
#    db.session.commit()
#    return jsonify({"message": "Student soft deleted"})
#
#

#@app.route("/students/all", methods=["GET"])
#def get_all_students():
#    students = Student.query.all()
#    result = [
#        {"id": s.id, "name": s.name, "is_deleted": s.is_deleted}
#        for s in students
#    ]
#    return jsonify(result)
#
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
#


#5. CSV File Upload and Download using Flask:
#--------------------------------------------





#import os
#import pandas as pd
#from flask import Flask, request, jsonify, send_file
#from flask_sqlalchemy import SQLAlchemy
#from flasgger import Swagger, swag_from
#
#app = Flask(__name__)
#
## Swagger Config
#swagger = Swagger(app)
#
## Folder to store uploaded CSV files
#UPLOAD_FOLDER = r"D:\Users\Murali\python\Python\Flask_files"
#os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
#app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#db = SQLAlchemy(app)
#
#
#class Student(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100))
#    age = db.Column(db.Integer)
#
#
#with app.app_context():
#    db.create_all()
#
#
#
#@swag_from({
#    "tags": ["CSV"],
#    "summary": "Upload CSV file",
#    "description": "Upload a CSV file containing name and age columns.",
#    "parameters": [
#        {
#            "name": "upload_csv",
#            "in": "formData",
#            "type": "file",
#            "required": True,
#            "description": "CSV file to upload"
#        }
#    ],
#    "responses": {
#        200: {
#            "description": "CSV uploaded successfully"
#        }
#    }
#})
#@app.route("/upload_csv", methods=["POST"])
#def upload_csv():
#
#    if "upload_csv" not in request.files:
#        return jsonify({"message": "No file uploaded"}), 400
#
#    file = request.files["upload_csv"]
#
#    if file.filename == "":
#        return jsonify({"message": "No file selected"}), 400
#
#    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
#    file.save(file_path)
#
#    df = pd.read_csv(file_path)
#
#    # Insert into DB
#    for _, row in df.iterrows():
#        student = Student(name=row["name"], age=row["age"])
#        db.session.add(student)
#
#    db.session.commit()
#
#    return jsonify({"message": "CSV uploaded successfully!"})
#
#
#
#@swag_from({
#    "tags": ["CSV"],
#    "summary": "Download CSV of all students",
#    "description": "Download all student records as a CSV file.",
#    "responses": {
#        200: {
#            "description": "CSV downloaded successfully"
#        }
#    }
#})
#@app.route("/download_csv", methods=["GET"])
#def download_csv():
#
#    students = Student.query.all()
#
#    data = {
#        "id": [s.id for s in students],
#        "name": [s.name for s in students],
#        "age": [s.age for s in students]
#    }
#
#    df = pd.DataFrame(data)
#    file_path = os.path.join(app.config["UPLOAD_FOLDER"], "students_data.csv")
#    df.to_csv(file_path, index=False)
#
#    return send_file(file_path, as_attachment=True)
#
#
#
#@swag_from({
#    "tags": ["Students"],
#    "summary": "Get all students",
#    "description": "Fetch all students from the database.",
#    "responses": {
#        200: {
#            "description": "List of students",
#        }
#    }
#})
#@app.route("/students", methods=["GET"])
#def get_students():
#    students = Student.query.all()
#    result = [{"id": s.id, "name": s.name, "age": s.age} for s in students]
#    return jsonify(result)
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
#
#
#
##Swagger for employee model with documentation:
#------------------------------------------------
#
#
#from flask import Flask, request, jsonify
#from flasgger import Swagger
#from flask_sqlalchemy import SQLAlchemy
#import os
#
#app = Flask(__name__)
#
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#db = SQLAlchemy(app)
#
#
#swagger = Swagger(app)
#
#
#class Employee(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50))
#    age = db.Column(db.Integer)
#
#
#@app.route("/employee", methods=["POST"])
#def create_employee():
#    """
#    Create a New Employee
#    ---
#    tags:
#      - Employee
#    parameters:
#      - name: body
#        in: body
#        required: true
#        schema:
#          id: Employee
#          required:
#            - name
#            - age
#          properties:
#            name:
#              type: string
#              example: "Ravi"
#            age:
#              type: integer
#              example: 28
#    responses:
#      200:
#        description: Employee created successfully
#    """
#    data = request.json
#    emp = Employee(name=data["name"], age=data["age"])
#    db.session.add(emp)
#    db.session.commit()
#    return jsonify({"message": "Employee created", "id": emp.id})
#
#
#
#@app.route("/employee", methods=["GET"])
#def get_employees():
#    """
#    Get All Employees
#    ---
#    tags:
#      - Employee
#    responses:
#      200:
#        description: List of all employees
#    """
#    employees = Employee.query.all()
#    data = [{"id": e.id, "name": e.name, "age": e.age} for e in employees]
#    return jsonify(data)
#
#
#
#@app.route("/employee/<int:id>", methods=["GET"])
#def get_employee(id):
#    """
#    Get Employee by ID
#    ---
#    tags:
#      - Employee
#    parameters:
#      - name: id
#        in: path
#        type: integer
#        required: true
#    responses:
#      200:
#        description: Employee details
#    """
#    emp = Employee.query.get_or_404(id)
#    return jsonify({"id": emp.id, "name": emp.name, "age": emp.age})
#
#
#
#@app.route("/employee/<int:id>", methods=["PUT"])
#def update_employee(id):
#    """
#    Update Employee
#    ---
#    tags:
#      - Employee
#    parameters:
#      - name: id
#        in: path
#        required: true
#        type: integer
#      - name: body
#        in: body
#        required: true
#        schema:
#          id: EmployeeUpdate
#          properties:
#            name:
#              type: string
#              example: "Updated Name"
#            age:
#              type: integer
#              example: 30
#    responses:
#      200:
#        description: Employee updated successfully
#    """
#    emp = Employee.query.get_or_404(id)
#    data = request.json
#
#    emp.name = data.get("name", emp.name)
#    emp.age = data.get("age", emp.age)
#
#    db.session.commit()
#    return jsonify({"message": "Employee updated"})
#
#
#
#@app.route("/employee/<int:id>", methods=["DELETE"])
#def delete_employee(id):
#    """
#    Delete Employee
#    ---
#    tags:
#      - Employee
#    parameters:
#      - name: id
#        in: path
#        required: true
#        type: integer
#    responses:
#      200:
#        description: Employee deleted successfully
#    """
#    emp = Employee.query.get_or_404(id)
#    db.session.delete(emp)
#    db.session.commit()
#    return jsonify({"message": "Employee deleted"})
#
#
#
#if __name__ == "__main__":
#    if not os.path.exists("employees.db"):
#        with app.app_context():
#            db.create_all()
#
#    app.run(debug=True)
import json
import pytest

from app import create_app, db

@pytest.fixture
def app():
    config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(test_config=config)
    # create tables
    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_employee_missing_fields(client):
    resp = client.post("/employees", json={"name": "Alice"})
    assert resp.status_code == 400
    assert resp.get_json().get("error") == "missing fields"


def test_create_employee_success(client):
    payload = {"name": "Bob", "department": "Engineering", "salary": 70000}
    resp = client.post("/employees", json=payload)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "Bob"
    assert data["department"] == "Engineering"
    assert float(data["salary"]) == 70000.0
    assert "id" in data


def test_get_employees(client):
    # create two
    client.post("/employees", json={"name": "A", "department": "D1", "salary": 100})
    client.post("/employees", json={"name": "B", "department": "D2", "salary": 200})
    resp = client.get("/employees")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_get_employee_not_found(client):
    resp = client.get("/employees/999")
    assert resp.status_code == 404
    assert resp.get_json().get("error") == "Employee not found"


def test_update_and_delete_employee(client):
    # create
    resp = client.post("/employees", json={"name": "C", "department": "D", "salary": 300})
    emp = resp.get_json()
    emp_id = emp["id"]

    # update
    upd = {"name": "C2", "salary": 350}
    resp = client.put(f"/employees/{emp_id}", json=upd)
    assert resp.status_code == 201
    updated = resp.get_json()
    assert updated["name"] == "C2"
    assert float(updated["salary"]) == 350.0

    # delete
    resp = client.delete(f"/employees/{emp_id}")
    assert resp.status_code == 204

    # ensure gone
    resp = client.get(f"/employees/{emp_id}")
    assert resp.status_code == 404

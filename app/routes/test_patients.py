from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_patients():
    response = client.get("/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_create_patients():
    response = client.post("/patients",
        json={
        "firstName": "Bob",
        "lastName": "Boby",
        "age": 40,
        "email": "bob@example.com",
        "phone": "0612345678"
        },         
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["firstName"] == "Bob"
    
def test_create_patient_invalid_age_type():
    response = client.post("/patients",
        json={
        "firstName": "Paca",
        "lastName": "Ping",
        "age": "one",
        "email": "paca@example.com",
        "phone": "0612345678"
        },         
    )
    assert response.status_code == 422 ## Unprocessable Entity
    
def test_update_patient():

    post_response = client.post("/patients", json={
        "firstName": "Martin",
        "lastName": "Test",
        "age": 30,
        "email": "martin@example.com",
        "phone": "0611223344"
    })
    assert post_response.status_code == 200
    patient_id = post_response.json()["id"]

    update_response = client.put(f"/patients/{patient_id}", json={
        "firstName": "MartinUpdated"
    })
    assert update_response.status_code == 200
    assert update_response.json()["firstName"] == "MartinUpdated"
    
def test_delete_patient():
    
    post_response = client.post("/patients", json={
        "firstName": "ToDelete",
        "lastName": "Temp",
        "age": 25,
        "email": "temp@example.com",
        "phone": "0677889900"
    })
    assert post_response.status_code == 200
    patient_id = post_response.json()["id"]

    delete_response = client.delete(f"/patients/{patient_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True}
    
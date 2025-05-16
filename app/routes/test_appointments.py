from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_appointment():
    
    # Create a patient
    response = client.post("/patients",
        json={
        "firstName": "Bob",
        "lastName": "Boby",
        "age": 40,
        "email": "boby@example.com",
        "phone": "0612345678"
        },         
    )
    assert response.status_code == 200
    patient_id = response.json()["id"]
        
    response = client.post("/appointments",
        json={
            "time": "2045-05-16",
            "reason": "consultation",
            "doctor": "Bob",
            "patient_id": patient_id
        },         
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["doctor"] == "Bob"
    
def test_list_appointments():
    
    # Create a patient
    response = client.post("/patients",
        json={
        "firstName": "Tom",
        "lastName": "Toby",
        "age": 40,
        "email": "tom@example.com",
        "phone": "0612345678"
        },         
    )
    assert response.status_code == 200
    patient_id = response.json()["id"]
    
    # Create un appointment
    response = client.post("/appointments",
        json={
            "time": "2045-05-16",
            "reason": "consultation",
            "doctor": "Dr. Bob",
            "patient_id": patient_id
        },         
    )
    assert response.status_code == 200
    
    response = client.get(f"/patients/{patient_id}/appointments")
    assert response.status_code == 200
    
    appointments = response.json()
    assert isinstance(appointments, list)
    assert len(appointments) >= 1
    assert appointments[0]["doctor"] == "Dr. Bob"
    assert appointments[0]["patient_id"] == patient_id

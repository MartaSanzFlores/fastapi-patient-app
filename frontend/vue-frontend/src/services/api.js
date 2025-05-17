const API_URL = "http://localhost:8000";

export async function getPatients() {
    const res = await fetch(`${API_URL}/patients`);
    return await res.json();
}

export async function postPatient(data) {
    const res = await fetch(`${API_URL}/patients`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (!res.ok) {
        alert("Creation Patient Error");
        return null;
    }

    return await res.json();
}

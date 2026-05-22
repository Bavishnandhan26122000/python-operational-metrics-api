from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Operational Metrics API"}

def test_get_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "cpu_usage" in data
    assert "memory_usage" in data
    assert "active_connections" in data
    assert "uptime_seconds" in data

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

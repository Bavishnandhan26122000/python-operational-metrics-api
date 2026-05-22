from fastapi import FastAPI
import random
import time

app = FastAPI(title="Operational Metrics API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Operational Metrics API"}

@app.get("/metrics")
def get_metrics():
    """Mock operational metrics"""
    return {
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(20.0, 80.0), 2),
        "active_connections": random.randint(100, 5000),
        "uptime_seconds": int(time.time() % 100000)
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

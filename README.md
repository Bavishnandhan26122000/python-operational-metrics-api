# Python Operational Metrics API

A lightweight Python REST API (using FastAPI) designed to mock system metrics and data processing, perfect for tying into data science and operational workflows.

## Features
- **FastAPI**: High performance REST API framework.
- **Dockerized**: Easy to build and deploy.
- **GitHub Actions**: Fully automated CI/CD pipeline.
- **SonarQube Integration**: Quality gates and code coverage requirements.

## CI/CD Pipeline
This project demonstrates a complete GitHub Actions workflow that:
1. Runs unit tests and enforces >80% code coverage.
2. Triggers a SonarQube code quality scan.
3. Fails the build if the code coverage is too low.
4. Builds and pushes a Docker image to a registry.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Run tests:
   ```bash
   pytest
   ```

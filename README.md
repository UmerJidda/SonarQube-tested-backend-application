# SonarQube Tested Backend Application

[![Python Tests](https://github.com/UmerJidda/SonarQube-tested-backend-application/actions/workflows/python-tests.yml/badge.svg)](https://github.com/UmerJidda/SonarQube-tested-backend-application/actions/workflows/python-tests.yml)

## Overview

This project demonstrates a DevSecOps-oriented backend application integrated with:

- Unit testing
- Code coverage analysis
- SonarQube static code analysis
- GitHub Actions CI/CD
- Security hotspot detection
- Secure SDLC concepts

The project was created as a proof-of-concept environment for validating automated code quality and security testing workflows.

---

## Features

- FastAPI backend application
- Automated unit testing with pytest
- Coverage reporting with pytest-cov
- Local SonarQube integration
- GitHub Actions CI pipeline
- Intentional vulnerable code patterns for AppSec demonstrations

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI |
| Testing | pytest |
| Coverage | pytest-cov |
| Static Analysis | SonarQube |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Language | Python 3.11+ |

---

## Project Structure

```text
SonarQube-tested-backend-application/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── __init__.py
│
├── tests/
│   ├── test_tasks.py
│   └── test_auth.py
│
├── .github/workflows/
│   └── python-tests.yml
│
├── docker-compose.yml
├── sonar-project.properties
├── requirements.txt
└── README.md
```

---

## Running The Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

---

## Running Unit Tests

```bash
pytest
```

---

## Generating Coverage Report

```bash
pytest --cov=app --cov-report=xml
```

This generates:

```text
coverage.xml
```

---

## Running SonarQube

Start SonarQube locally:

```bash
docker compose up -d
```

Access dashboard:

```text
http://localhost:9000
```

Run analysis:

```powershell
pysonar `
  --sonar-host-url=http://localhost:9000 `
  --sonar-token=YOUR_TOKEN `
  --sonar-project-key=SonarQube-tested-backend-application
```

---

## GitHub Actions CI/CD

The GitHub Actions workflow automatically:

- Installs dependencies
- Runs unit tests
- Generates coverage reports

Triggered on:
- Push to main
- Pull requests to main

---

## Intentional Security Vulnerabilities

This project intentionally includes insecure coding patterns for educational and DevSecOps demonstration purposes.

Examples include:

- Hardcoded secrets
- eval() usage
- Weak randomness generation
- Duplicate logic
- Untested functions

These are included to demonstrate:
- Security hotspot detection
- Static Application Security Testing (SAST)
- Secure SDLC validation workflows

---

## Security Concepts Demonstrated

- Shift-left security
- Static code analysis
- Secure coding validation
- CI/CD automation
- Coverage analysis
- Security hotspot detection
- DevSecOps pipeline integration

---

## Future Improvements

Potential future enhancements include:

- SonarQube Quality Gates
- Container vulnerability scanning
- IaC security scanning
- Dockerized backend deployment
- Branch protection policies
- Automated security enforcement

---

## Disclaimer

This project contains intentionally vulnerable code strictly for educational, testing, and DevSecOps demonstration purposes.
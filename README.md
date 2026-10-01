# Patient Management System API

A REST API built with **FastAPI** and **Python** for managing patient records with automatic BMI calculation and health verdict generation. Integrated with Docker and GitHub Actions CI/CD pipeline.

---

## DevOps Integration

### Tool 1 — Docker
This project is fully containerized using Docker.
- Consistent environment across all machines
- Single command deployment
- Publicly available on Docker Hub

### Tool 2 — GitHub Actions CI/CD
Automated pipeline triggers on every push to main branch.
- Automatically builds Docker image
- Automatically pushes to Docker Hub
- Zero manual deployment steps

---

## Features

- Add, view, update and delete patient records
- Automatic BMI calculation from height and weight
- Health verdict generation (Underweight, Normal, Overweight, Obese)
- Sort patients by height or weight
- Input validation using Pydantic
- Interactive API documentation via Swagger UI

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.14 |
| Framework | FastAPI |
| Validation | Pydantic |
| Server | Uvicorn |
| Container | Docker |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| OS | Ubuntu (Linux) |

---

## Run With Docker (Recommended)

```bash
# Pull the image
docker pull aaryanparave/patient-management-api:latest

# Run the container
docker run -d -p 8000:8000 \
  --name patient-api \
  aaryanparave/patient-management-api:latest
```

Open API docs at: http://localhost:8000/docs or http://127.0.0.1:8000/docs

---

## Run Locally

1. Clone the repository
```bash
   git clone https://github.com/aaryan-parave/patient-management-api.git
   cd patient-management-api
```

2. Create virtual environment
```bash
   python3 -m venv myenv
   source myenv/bin/activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Run the server
```bash
   uvicorn main:app --reload
```

5. Open docs
http://localhost:8000/docs or http://127.0.0.1:8000/docs

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /about | About the API |
| GET | /view | View all patients |
| GET | /patient/{id} | View single patient |
| GET | /sort | Sort by height or weight |
| POST | /create | Add new patient |
| PUT | /update/{id} | Update patient |
| DELETE | /delete/{id} | Delete patient |

---

## Patient Data Model

| Field | Type | Validation |
|-------|------|-----------|
| id | string | Unique patient ID |
| name | string | Patient full name |
| city | string | City of residence |
| age | integer | Between 1 and 120 |
| gender | string | Male, Female, Other |
| height | float | In meters, above 0 |
| weight | float | In kgs, above 0 |
| bmi | float | Auto-calculated |
| verdict | string | Auto-generated |

---

## CI/CD Pipeline

Pipeline triggers automatically on every push to main branch:
git push → GitHub Actions triggered →Fresh Ubuntu VM spins up →Code checked out →Docker image built →Image pushed to Docker Hub with 2 tags →:latest and :commit-sha

---

## Project Structure


patient-management-api/
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline
├── main.py                 # FastAPI application
├── patients.json           # Data storage
├── requirements.txt        # Dependencies
├── Dockerfile              # Container configuration
├── .gitignore              # Git ignore rules
└── README.md               # Documentation


---

## Docker Hub

Public image available at:

docker pull aaryanparave/patient-management-api:latest


---


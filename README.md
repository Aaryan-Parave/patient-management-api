# Patient Management System API

A RESTful API built with FastAPI for managing patient records. It supports CRUD operations, automatic BMI calculation, and weight category classification based on patient data.

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## Features
- Create, Read, Update, and Delete the patient's record
- Automatic BMI calculation 
- weight category classification 
- Sort patient by height or weight
- JSON file-based data storage

## Run Locally

1. Clone the repo
```bash
git clone git@github.com:Aaryan-Parave/patient-management-api.git
```

2. Create virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn main:app --reload
```

5. Open API docs
Open: http://127.0.0.1:8000/docs

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

## Project Structure
```text 
FastAPI/
├── main.py          # Main application
├── patients.json    # Patient data storage
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

# Patient Management System API

A REST API built with FastAPI to manage patient records 
with automatic BMI calculation and weight verdict.

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## Run Locally

1. Clone the repo
   git clone <your-repo-url>

2. Create virtual environment
   python -m venv myenv
   myenv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the server
   uvicorn main:app --reload

5. Open API docs
   http://127.0.0.1:8000/docs

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

FastAPI/
├── main.py          # Main application
├── patients.json    # Patient data storage
├── requirements.txt # Dependencies
└── README.md        # Documentation
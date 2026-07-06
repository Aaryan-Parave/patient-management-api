from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description= "ID of the Patient", example= "P001")]
    name: Annotated[str, Field(..., description= "Name of the Patient")]
    city: Annotated[str, Field(..., description= "City of the Patient")]
    age: Annotated[int, Field(..., gt= 0, lt= 120, description= "Age of the Patient")]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description= "Gender of the Patient")]
    height: Annotated[float, Field(..., gt= 0, description= "Height of the Patient in meters")]
    weight: Annotated[float, Field(..., gt= 0, description= "Weight of the Patient in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity" 


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description= "Name of the Patient")]
    city: Annotated[Optional[str], Field(default=None, description= "City of the Patient")]
    age: Annotated[Optional[int], Field(default=None, gt= 0, lt= 120, description= "Age of the Patient")]
    gender: Annotated[Optional[Literal["Male", "Female", "Other"]], Field(default=None, description= "Gender of the Patient")]
    height: Annotated[Optional[float], Field(default=None, gt= 0, description= "Height of the Patient in meters")]
    weight: Annotated[Optional[float], Field(default=None, gt= 0, description= "Weight of the Patient in kgs")]

def load_data():
    with open ('patient.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'This is a Patient Management System API built using FastAPI.'}

@app.get('/view')
def view():
    data = load_data()
    return data 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description= "Patient ID to View", example= "P001")):
    # Load the patient data
    data  = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail = "Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'sort by field', example = 'height or weight'), order: str = Query('asc', description = 'sort in ascending or descending order')):
    
    valid_sort_fields = ['height', 'weight']

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code= 400, detail = f"Invalid sort field. Valid fields are: {', '.join(valid_sort_fields)}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code= 400, detail = "Invalid order. Valid orders are: 'asc' or 'desc'")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(order == 'desc'))
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    # Load the existing patient data
    data = load_data()

    # Check if the patient ID already Exists
    if patient.id in data:
        raise HTTPException(status_code= 400, detail= "Patient ID already Exists")

    # Enter the new patient data into the existing data
    data[patient.id] = patient.model_dump(exclude= ['id'])

    # Save the updated data back to the JSON file
    save_data(data)

    return JSONResponse(status_code= 201, content= {'message': 'Patient created successfully'})

@app.put('/update/{patient_id}')
def update_patient(patient_id: str = Path(..., description="Patient ID to update", example="P001"), patient_update: PatientUpdate = ...):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    updated_fields = patient_update.model_dump(exclude_unset=True, exclude_none=True)
    if not updated_fields:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    existing_patient_data = data[patient_id]
    existing_patient_data.update(updated_fields)

    patient_pydantic_obj = Patient(id=patient_id, **existing_patient_data)
    data[patient_id] = patient_pydantic_obj.model_dump(exclude={'id'})

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            'message': 'Patient updated successfully',
            'patient': patient_pydantic_obj.model_dump()
        }
    )

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not Found")
    
    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200, content= {'message': 'Patient deleted successfully'})
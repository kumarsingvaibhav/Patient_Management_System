from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from Database.models import Patient
from Configuration import patient_collection

app = FastAPI()

@app.get("/")
async def home():
    return {"msg": "Patient Management System"}

@app.get("/about")
async def about():
    return {"msg": "Fully Functional API to manage Patient Records"}

@app.get("/view")
async def view():
    patients = list(patient_collection.find({"is_deleted": False}))
    for p in patients:
        p["_id"] = str(p["_id"])
    return patients

@app.get("/patient/{patient_id}")
async def view_patient(
    patient_id: str = Path(
        ...,
        description="ID of the Patient",
        examples=["P001"],
    )
):
    patient = patient_collection.find_one({"patient_id": patient_id, "is_deleted": False})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    patient["_id"] = str(patient["_id"])
    return patient

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description="Sort by field"), order: str = Query("asc", description="asc or desc")):
    valid_fields = ["age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field. Select from {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Select 'asc' or 'desc'")

    order_flag = 1 if order == "asc" else -1
    patients = list(patient_collection.find({"is_deleted": False}).sort(sort_by, order_flag))
    for p in patients:
        p["_id"] = str(p["_id"])
    return patients

@app.post("/create")
def create_patient(patient: Patient):
    if patient_collection.find_one({"patient_id": patient.patient_id}):
        raise HTTPException(status_code=400, detail="Patient already exists")
    patient_dict = patient.model_dump()
    patient_collection.insert_one(patient_dict)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})

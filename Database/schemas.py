def individual_data(patient):
    return {
        "id": str(patient["_id"]),
        "patient_id": patient["patient_id"],
        "name": patient["name"],
        "age": patient["age"],
        "gender": patient["gender"],
        "blood_group": patient["blood_group"],
        "phone": patient["phone"],
        "email": patient["email"],
        "diagnosis": patient["diagnosis"],
        "admission_date": patient["admission_date"],
        "is_insured": patient["is_insured"],
        "height": patient["height"],
        "weight": patient["weight"],
        "is_completed": patient["is_completed"],
        "bmi": round(patient["weight"] / (patient["height"] ** 2), 2),
        "verdict": ("Underweight" if patient["weight"] / (patient["height"] ** 2) < 18.5
                    else "Normal" if patient["weight"] / (patient["height"] ** 2) < 25
                    else "Overweight" if patient["weight"] / (patient["height"] ** 2) < 30
                    else "Obese")
    }

def all_patients(patients):
    return [individual_data(p) for p in patients]

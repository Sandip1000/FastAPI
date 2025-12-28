from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


# Model validator is used when we have to validate the one data based on another data

class Patient(BaseModel):

    name : str
    email :EmailStr
    age : int
    weight: float
    married : bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @model_validator(mode ="after")   # mode = "after" means After Type Coercion
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model

   


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)



patient_info = {"name" : "sandip","email": "abc1234@gmail.com" ,"age": 65, "weight": 56.8, "married": True, "allergies":
                ["pollen", "dust"], "contact_details" : {"phone_number": "9758548874" , "emergency": "9876543567"}}
patient1 = Patient(**patient_info)  # Validation -> Type Coercion

insert_patient_data(patient1)
from pydantic import BaseModel, EmailStr,AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated



# Field validator is used for custom data validation according to our needs
class Patient(BaseModel):

    name : str
    email :EmailStr
    age : int
    weight: float
    married : bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        
        valid_domians = ["sumeru.com", "bnb.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domians:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator("age", mode= "after")  # mode = "after" means after  type coercion and default mode is after
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError(" Age should be in between 0 and 100")


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)



patient_info = {"name" : "sandip","email": "abc1234@sumeru.com" ,"age": "30", "weight": 56.8, "married": True, "allergies":
                ["pollen", "dust"], "contact_details" : {"phone_number": "9758548874"}}
patient1 = Patient(**patient_info)  # Validation -> Type Coercion

insert_patient_data(patient1)
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict



class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight: float  #kg
    height: float  #meter
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

    @computed_field 
    @property
    def calculate_bmi(self) -> float:    # BMI is calculated later
        bmi = round(self.weight/(self.height**2),2)
        return bmi




def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.calculate_bmi)



patient_info = {"name" : "sandip","email": "abc1234@gmail.com" ,"age": 65, "weight": 56.8, "height":1.72,"married": True, "allergies":
                ["pollen", "dust"], "contact_details" : {"phone_number": "9758548874"}}

patient1 = Patient(**patient_info)  

insert_patient_data(patient1)
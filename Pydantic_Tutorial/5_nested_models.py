from pydantic import BaseModel

class Address(BaseModel):

    city : str
    province : str
    pin : str


class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dict = {"city":"ktm", "province": "bagmati", "pin": "10045"}
address_1 = Address(**address_dict)

patient_dict = {"name": "sandip", "gender": "male", "age":30, "address": address_1}
patient_1 = Patient(**patient_dict)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address)
    print(patient.address.city)
    print("Inserted Into Database")


insert_patient_data(patient_1)


# Advantages

# 1. Better organization of related data(e.g. vitals, address, insurance)
# 2. Reusability : Use vitals in multiple models (e.g. Patient, MedicalRecord)
# 3. Readability : Easier for developers and API consumers to understand
# 4. Validation : Nested models are validated automatically - no extra work needed
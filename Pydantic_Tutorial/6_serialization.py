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

temp = patient_1.model_dump(include=["name", "gender"])   # Returns the pydantic object as a dictionary
print(temp)                                              # We can also use exclude include and exclude_unset with this function
print(type(temp))


temp = patient_1.model_dump_json()   # Returns the pydantic object as a json string
print(temp)
print(type(temp))
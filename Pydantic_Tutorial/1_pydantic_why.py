# Problem_1 = Type Validation

# Absence of the type validation
def insert_patient_data(name, age):
     
    print(name) # Here is some database related code
    print(age)
    print("Inserted Into Database")

insert_patient_data('nitish', 'thirty')




# Use of Type Hinting
# But the type hinting does not give an error so it lacks the data validation properly
def insert_patient_data(name : str, age : int):
     
    print(name)# Here is some database related code
    print(age)
    print("Inserted Into Database")

insert_patient_data('nitish', 10)



# Raising Exception
# This solve the previous error but it is not scalable
def insert_patient_data(name : str, age : int):

    if type(name) == str and type(age)==int: 
        print(name)         # Here is some database related code
        print(age)
        print("Inserted Into Database")
    else:
        raise TypeError("Incorrect Data Type")

insert_patient_data('nitish', 10)



def update_patient_data(name : str, age : int):

    if type(name) == str and type(age)==int: 
        print(name)        # Here is some database related code
        print(age)
        print("Updated")
    else:
        raise TypeError("Incorrect Data Type")
    
update_patient_data('nitish', 30)
    





# Problem_2 = Data Validation
def insert_patient_data(name : str, age : int):

    if type(name) == str and type(age)==int: 

        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            print(name)      # Here is some database related code
            print(age)
            print("Inserted Into Database")
    else:
        raise TypeError("Incorrect Data Type")

insert_patient_data('nitish', 10)



# Manually performing data validation and type validation is very hard in Python.
# So Pydantic is very useful for data validation and type validation.

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    #Type Validation and Data Validation
    name : Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 chars",
                                examples=["Nitish","Sandip"])]
    email : EmailStr                      # Data type of pydantic for validating email
    linkedin_url : AnyUrl                 # Data type of pydantic for vaildating URL
    age : int = Field(gt=0, lt=120)
    weight : Annotated[float, Field(gt=0 , strict=True)]
    married :Annotated[bool, Field(default=None, description=" Is the patient is married or not")]
    allergies : Optional[List[str]] = None # Two Level Validation that is validate list as well as the data type of each list item
                                           # Here None is the default value
    contact : Dict[str,str]                # This ensures key and value of dictionary are strings

patient_info = {"name" : "sandip","email": "abc1234@gmail.com" ,"linkedin_url": "https://linkedin.com/3345","age": 30, "weight": 56.8, "married": True, "allergies":
                ["pollen", "dust"], "contact" : {"phone_number": "9758548874"}}
patient1 = Patient(**patient_info)




def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Inserted")

insert_patient_data(patient1)
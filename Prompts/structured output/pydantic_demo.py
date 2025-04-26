from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {'name':'Soumya'}
student = Student(**new_student)
print (student)

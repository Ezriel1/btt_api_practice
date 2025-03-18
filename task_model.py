from pydantic import BaseModel #Fastapi runs behind a library called pydantic which makes sure that the parameters are the same type

cur_id = 0

def increment():
    global cur_id
    cur_id += 1
    return cur_id

class Task(BaseModel): #example of inheritence, it extends
    id: int
    description: str = ""
    isComplete: bool = False

    def __init__(self, **data):
        super().__init__(id= increment(), **data)
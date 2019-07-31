from pydantic import BaseModel

class Feedback(BaseModel):
    category : str
    content : str
    contant_no : str

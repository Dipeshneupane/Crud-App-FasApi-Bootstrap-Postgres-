from pydantic import BaseModel, Field

class WebSchema(BaseModel):
    id: int
    name: str

    class Database:
        orm_mode = True

class RequestWeb(BaseModel):
    parameter: WebSchema= Field(...)


from pydantic import BaseModel

class PropertyFeatures(BaseModel):
    LotArea: float
    OverallQual: int
    OverallCond: int
    CentralAir: str
    FullBath: int
    BedroomAbvGr: int
    GarageCars: int

class Feedback(BaseModel):
    id: int
    thumbs_up: int

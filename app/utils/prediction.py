import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from ..api.models import SalePricePredictionModel

from pydantic import BaseModel

scaler = StandardScaler()

model = SalePricePredictionModel(input_size=7)
model.load_state_dict(torch.load("checkpoints/model.pth", weights_only=True))
model.eval()

class InputData(BaseModel):
    lot_area: float
    overall_quality: float
    overall_condition: float
    central_air: int  # Assuming binary (0 or 1)
    full_bath: int    # Number of full bathrooms
    bedrooms: int     # Number of bedrooms
    garage_cars: int  # Number of garage cars

def predictPrice(data: InputData):
    # Convert input data to tensor
    input_tensor = np.array([[
        data["lot_area"],
        data["overall_quality"],
        data["overall_condition"],
        data["central_air"],
        data["full_bath"],
        data["bedrooms"],
        data["garage_cars"]
    ]], dtype=np.float32)
    
    input_tensor = scaler.fit_transform(input_tensor)
    input_tensor = torch.from_numpy(input_tensor)
    
    # Run the model
    with torch.no_grad():
        prediction = model(input_tensor)

    # Return the result as JSON
    item = prediction.item()
    return item * 10**6

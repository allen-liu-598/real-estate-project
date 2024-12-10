import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from ..api.models import SalePricePredictionModel

from pydantic import BaseModel

scaler = StandardScaler()

model = SalePricePredictionModel(input_size=7)
model.load_state_dict(torch.load("checkpoints/model.pth", weights_only=True))
model.eval()

def predictPrice(lot_area, overall_quality, overall_condition, central_air, full_bath, bedrooms, garage_cars):
    # Convert input data to tensor
    input_tensor = np.array([[
        lot_area,
        overall_quality,
        overall_condition,
        central_air,
        full_bath,
        bedrooms,
        garage_cars
    ]], dtype=np.float32)
    
    input_tensor = scaler.fit_transform(input_tensor)
    input_tensor = torch.from_numpy(input_tensor)
    
    # Run the model
    with torch.no_grad():
        prediction = model(input_tensor)

    # Return the result as JSON
    item = prediction.item()
    return item * 10**6

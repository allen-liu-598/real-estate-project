import pandas as pd
import torch
from model import SalePricePredictionModel
data = {
    "Lot Area": [31770],
    "Overall Qual": [7],
    "Overall Cond": [5],
    "Central Air": [1],
    "Full Bath": [2],
    "Bedroom": [3],
    "Garage Cars": [2],
}

df = pd.DataFrame(data)

data = torch.tensor(df.values, dtype=torch.float32)
print(data)
input_size = data.shape[1]

model = SalePricePredictionModel(input_size)
model.load_state_dict(torch.load("checkpoints/model.pth"))

model.eval()
output = model(data)

print(output * 10**6)
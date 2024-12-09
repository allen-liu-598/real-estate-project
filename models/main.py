import pandas as pd
import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from model import SalePricePredictionModel

torch.set_printoptions(threshold=float('inf'))

file_path = "data/raw/AmesHousing.csv"
data = pd.read_csv(file_path) 

data['data_source'] = 1

columns_to_keep = ["SalePrice", "Lot Area", "Overall Qual", "Overall Cond", 
                   "Central Air", "Full Bath", "Bedroom AbvGr", "Garage Cars"]

data = data[columns_to_keep]
data['Central Air'] = data['Central Air'].replace({'Y': 1, 'N': 0})
data = data.dropna()

X = data.drop("SalePrice", axis=1)
y = data["SalePrice"] / 10**6

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert data to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

input_size = X_train.shape[1]
model = SalePricePredictionModel(input_size)

model.load_state_dict(torch.load('checkpoints/model.pth'))
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 10000
for epoch in range(epochs):
    # Forward pass
    predictions = model(X_train_tensor)
    loss = criterion(predictions, y_train_tensor)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Print loss every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
    
torch.save(model.state_dict(), 'checkpoints/model.pth')

model.eval()
with torch.no_grad():
    predictions = model(X_test_tensor)
    test_loss = criterion(predictions, y_test_tensor)
    print(f'Test Loss: {predictions * 10**6}')
    

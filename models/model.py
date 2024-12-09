import torch.nn as nn

class SalePricePredictionModel(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 256),   # Increase neurons in the first layer
            nn.ReLU(),
            nn.Dropout(0.3),              # Increase dropout for regularization
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)              # Output layer
        )
    
    def forward(self, x):
        return self.fc(x)
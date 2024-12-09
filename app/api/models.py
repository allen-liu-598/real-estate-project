from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RealEstate(Base):
    __tablename__ = 'real_estate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    LotArea = Column(Float)
    OverallQual = Column(Integer)
    OverallCond = Column(Integer)
    CentralAir = Column(String)
    FullBath = Column(Integer)
    BedroomAbvGr = Column(Integer)
    GarageCars = Column(Integer)
    SalePrice = Column(Float)
    data_source = Column(Integer)
    thumbs_up = Column(Integer, default=0)  # For RLHF feedback

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
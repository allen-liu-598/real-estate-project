import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String

# Constants
DATABASE_FILE = "data/database.sqlite"
RAW_DATA_FILE = "data/raw/AmesHousing.csv"
TABLE_NAME = "real_estate"

# Step 1: Create Database Connection
def get_engine():
    os.makedirs("data", exist_ok=True)
    db_url = f"sqlite:///{DATABASE_FILE}"
    engine = create_engine(db_url)
    return engine

# Step 2: Create the Database Schema
def create_schema(engine):
    metadata = MetaData()
    real_estate_table = Table(
        TABLE_NAME,
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("LotArea", Float),
        Column("OverallQual", Integer),
        Column("OverallCond", Integer),
        Column("CentralAir", String),
        Column("FullBath", Integer),
        Column("BedroomAbvGr", Integer),
        Column("GarageCars", Integer),
        Column("SalePrice", Float),
        Column("data_source", Integer),  # New column for data source
    )
    metadata.create_all(engine)
    print(f"Database schema created in {DATABASE_FILE}.")

# Step 3: Load Data into the Database
def load_data(engine):
    # Read the CSV file
    df = pd.read_csv(RAW_DATA_FILE)

    # Select relevant columns and preprocess
    df = df[
        ["LotArea", "OverallQual", "OverallCond", "CentralAir", 
         "FullBath", "BedroomAbvGr", "GarageCars", "SalePrice"]
    ]
    df["data_source"] = 1  # Mark all rows with data_source = 1 (Ames dataset)

    # Write data to the database
    df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into the database.")

# Main Execution
if __name__ == "__main__":
    engine = get_engine()
    create_schema(engine)
    load_data(engine)
    print("Database setup complete.")

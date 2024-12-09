from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import RealEstate

DATABASE_FILE = "data/database.sqlite"
TABLE_NAME = "real_estate"

# Database connection setup
def get_engine():
    return create_engine(f"sqlite:///{DATABASE_FILE}")

# Function to query similar properties
def get_similar_properties(features):
    engine = get_engine()

    # Create a session for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Build the query with filtering conditions based on the features provided
    query = session.query(RealEstate).filter(
        RealEstate.LotArea.between(features['LotArea'] - 500, features['LotArea'] + 500),
        RealEstate.OverallQual.between(features['OverallQual'] - 1, features['OverallQual'] + 1),
        RealEstate.GarageCars == features['GarageCars']
    )

    # Limit results for efficiency (top 5)
    similar_properties = query.limit(5).all()

    # Convert the result to a list of dictionaries to return in the response
    result = [{
        "id": property.id,
        "LotArea": property.LotArea,
        "OverallQual": property.OverallQual,
        "OverallCond": property.OverallCond,
        "CentralAir": property.CentralAir,
        "FullBath": property.FullBath,
        "BedroomAbvGr": property.BedroomAbvGr,
        "GarageCars": property.GarageCars,
        "SalePrice": property.SalePrice,
        "data_source": property.data_source
    } for property in similar_properties]

    session.close()

    return result

def record_feedback(id, thumbs_up):
    return
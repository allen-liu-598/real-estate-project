from fastapi import FastAPI, HTTPException
from .api.routes import router

from .utils.prediction import predictPrice

app = FastAPI()

@app.get("/")

async def predict():
    try:
        data = {
            "lot_area": 8000,
            "overall_quality": 7,
            "overall_condition": 5,
            "central_air": 1,
            "full_bath": 2,
            "bedrooms": 3,
            "garage_cars": 2,
        }
        
        return {"predicted_price": predictPrice(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
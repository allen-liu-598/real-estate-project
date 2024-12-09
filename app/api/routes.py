from fastapi import APIRouter, HTTPException
from .database import get_similar_properties, record_feedback
from .schemas import PropertyFeatures, Feedback

router = APIRouter()

# Endpoint to fetch similar properties
@router.post("/similar-properties/")
async def get_properties(features: PropertyFeatures):
    try:
        properties = get_similar_properties(features.dict())
        if not properties:
            raise HTTPException(status_code=404, detail="No similar properties found.")
        return properties
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to record feedback for RLHF
@router.post("/record-feedback/")
async def record_user_feedback(feedback: Feedback):
    try:
        record_feedback(feedback.id, feedback.thumbs_up)
        return {"message": "Feedback recorded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

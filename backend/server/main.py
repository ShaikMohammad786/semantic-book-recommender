from fastapi import FastAPI
from pydantic import BaseModel
from core.recommender_pipeline import SemanticRecommendation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendationRequest(BaseModel):
    query:str
    category:str
    emotion:str
    top_k:int



@app.get("/")
def read_root():
    return {"hello world"}


@app.post("/recommendations")
def get_semantic_recommendations(request:RecommendationRequest):
    query= request.query
    category = request.category
    tone = request.emotion
    top_k = request.top_k

    try:
        semantic_recommender = SemanticRecommendation(
            query,
            category,
            tone,
            top_k
        )

    except Exception as e:
        print(e)
        
    ranked_books =semantic_recommender.pipeline()

    books = ranked_books.fillna("")

    return {"books": books.to_dict(
        orient="records"
    )}








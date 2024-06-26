from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
from fastapi.middleware.cors import CORSMiddleware
from services.genai import (YoutubeProcessor,
                            GeminiProcessor)
import os

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    #advanced settings
    
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai_processor = GeminiProcessor(model_name="gemini-pro",
                                      project="single-being-421820")

@app.post("/analyze_video")
def analyze_video(request: VideoAnalysisRequest):

    
    processor = YoutubeProcessor(genai_processor=genai_processor)
    
    result = processor.retrieve_youtube_documents(str(request.youtube_link),verbose=True)
    
    key_concepts = processor.find_key_concepts(result,verbose=True)
    
    
    return {
            "key_concepts": key_concepts
            }

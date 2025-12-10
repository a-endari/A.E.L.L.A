from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.services.translation import definition_grabber_async
from app.services.pronunciation import get_audio_url_async
from app.services.text_processing import remove_article

app = FastAPI(title="Universal Language App API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WordRequest(BaseModel):
    word: str

@app.get("/")
def read_root():
    return {"message": "Universal Language App API is running"}

@app.post("/api/lookup")
async def lookup_word(request: WordRequest):
    raw_word = request.word.strip()
    if not raw_word:
        raise HTTPException(status_code=400, detail="Word cannot be empty")

    # Clean word for processing (removing articles etc)
    clean_word = remove_article(raw_word)

    # Fetch data in parallel
    definition_future = definition_grabber_async(clean_word)
    audio_future = get_audio_url_async(clean_word)

    definition = await definition_future
    audio_url = await audio_future

    return {
        "original_word": raw_word,
        "clean_word": clean_word,
        "definition": definition,
        "audio_url": audio_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

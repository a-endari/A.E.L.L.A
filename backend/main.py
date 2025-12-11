from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.services.translation import translate_text_async, scrape_persian_definitions
from app.services.synonyms import get_synonyms_async
from app.services.pronunciation import get_audio_url_async
from app.services.text_processing import remove_article
from app.services.anki import create_deck
from app.services.obsidian import create_obsidian_zip
from fastapi.responses import Response

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
    include_persian: bool = True

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
    # Replacing specialized grabber with generic translator as requested    # Run tasks concurrently
    # definition_future = definition_grabber_async(clean_word) # Old
    
    definition_future = None
    if request.include_persian:
        definition_future = scrape_persian_definitions(clean_word) # New
    
    audio_future = get_audio_url_async(clean_word)
    
    english_future = translate_text_async(clean_word, source='de', target='en')
    
    synonyms_future = get_synonyms_async(clean_word)

    definitions_list = await definition_future if definition_future else []
    audio_data = await audio_future
    english_definition = await english_future
    synonyms = await synonyms_future

    audio_url = audio_data.get("audio_url") if audio_data else None
    canonical_word = audio_data.get("canonical_word") if audio_data else None

    # Use canonical word (with correct article) as clean_word for display if available
    # Otherwise fallback to the locally cleaned word
    final_display_word = canonical_word if canonical_word else clean_word

    return {
        "original_word": raw_word,
        "clean_word": final_display_word, # Updates the main display to be "das Haus"
        "definitions": definitions_list, # List[str]
        "english_definition": english_definition,
        "synonyms": synonyms,
        "audio_url": audio_url
    }

class AnkiRequest(BaseModel):
    cards: list[dict]

@app.post("/api/anki/download")
async def download_anki_deck(request: AnkiRequest):
    deck_stream = create_deck(request.cards)
    headers = {'Content-Disposition': 'attachment; filename="UniversalLanguageDeck.apkg"'}
    return Response(content=deck_stream.read(), media_type="application/octet-stream", headers=headers)

@app.post("/api/obsidian/download")
async def download_obsidian_zip(request: AnkiRequest):
    # Reusing AnkiRequest since the data structure (list of cards) is the same
    zip_stream = await create_obsidian_zip(request.cards)
    headers = {'Content-Disposition': 'attachment; filename="UniversalLanguageObsidian.zip"'}
    return Response(content=zip_stream.read(), media_type="application/zip", headers=headers)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

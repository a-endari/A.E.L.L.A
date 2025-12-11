import os
import edge_tts
import re
from typing import Dict, Optional

STATIC_AUDIO_DIR = "static/audio"
BASE_URL = "http://localhost:8000"

def sanitize_filename(text: str) -> str:
    """Make text safe for filesystem."""
    # Remove invalid chars
    clean = re.sub(r'[^\w\-\.]', '_', text)
    return clean

async def get_audio_url_async(german_word: str) -> Dict[str, Optional[str]]:
    """
    Generates audio for the given word using Microsoft Edge TTS (free neural voices).
    Saves to local static folder and returns the URL.
    """
    if not german_word:
        return {"audio_url": None, "canonical_word": None}

    clean_filename = sanitize_filename(german_word) + ".mp3"
    file_path = os.path.join(STATIC_AUDIO_DIR, clean_filename)
    
    # Check if exists (Simple caching)
    if not os.path.exists(file_path):
        try:
            # Generate Audio
            # Voice options: de-DE-KatjaNeural, de-DE-ConradNeural, etc.
            communicate = edge_tts.Communicate(german_word, "de-DE-KatjaNeural")
            await communicate.save(file_path)
        except Exception as e:
            print(f"Error generating TTS for {german_word}: {e}")
            return {"audio_url": None, "canonical_word": german_word}

    # Return the URL
    full_url = f"{BASE_URL}/{STATIC_AUDIO_DIR}/{clean_filename}"
    
    return {
        "audio_url": full_url,
        "canonical_word": german_word  # We don't have a scraper to tell us the "official" word anymore
    }

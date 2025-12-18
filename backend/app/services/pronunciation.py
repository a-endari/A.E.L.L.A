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

async def get_audio_url_async(text: str, voice: str = "de-DE-KatjaNeural") -> Dict[str, Optional[str]]:
    """
    Generates audio for the given word using Microsoft Edge TTS (free neural voices).
    Saves to local static folder and returns the URL.
    """
    if not text:
        return {"audio_url": None, "original_text": None}

    # Sanitize filename: text_voice.mp3 to avoid collisions between languages
    # e.g. "chat" (French) vs "chat" (English)
    safe_text = sanitize_filename(text)
    safe_voice = sanitize_filename(voice)
    clean_filename = f"{safe_text}_{safe_voice}.mp3"
    
    file_path = os.path.join(STATIC_AUDIO_DIR, clean_filename)
    
    # Check if exists (Simple caching)
    if not os.path.exists(file_path):
        try:
            # Generate Audio
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(file_path)
        except Exception as e:
            print(f"Error generating TTS for {text} ({voice}): {e}")
            return {"audio_url": None, "original_text": text}

    # Return the URL
    full_url = f"{BASE_URL}/{STATIC_AUDIO_DIR}/{clean_filename}"
    
    return {
        "audio_url": full_url,
        "original_text": text
    }

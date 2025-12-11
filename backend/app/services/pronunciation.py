import os
import requests
import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup

def get_audio_url(german_word):
    url = f"https://dic.b-amooz.com/de/dictionary/w?word={german_word.lower()}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.78 Safari/537.36",
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return parse_audio_url(response.text)
    except Exception as e:
        print(f"Error getting audio url: {e}")
    return None


def parse_audio_url(html):
    """Parse HTML to extract audio URL and the canonical word (with article)"""
    soup = BeautifulSoup(html, "html.parser")
    
    audio_link = None
    canonical_word = None

    # Try to find the canonical word (e.g. "das Haus")
    h1 = soup.find("h1", class_="mdc-typography--headline4 ltr d-inline position-relative")
    if h1:
        canonical_word = h1.get_text(strip=True)

    # Try the original method first for audio
    if h1 and h1.find("small") and "data-url" in h1.find("small").attrs:
        audio_link = h1.find("small")["data-url"]
        
    if not audio_link:
        # Alternative method - look for any audio element
        audio_elements = soup.find_all("audio")
        for audio in audio_elements:
            if audio.has_attr("src"):
                audio_link = audio["src"]
                break
            
    if not audio_link:
        # Try to find any element with data-url attribute
        elements_with_data_url = soup.find_all(attrs={"data-url": True})
        if elements_with_data_url:
            audio_link = elements_with_data_url[0]["data-url"]
    
    return {"audio_url": audio_link, "canonical_word": canonical_word}

async def get_audio_url_async(german_word: str) -> str | None:
    """Async version of get_audio_url"""
    url = f"https://dic.b-amooz.com/de/dictionary/w?word={german_word.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.78 Safari/537.36",
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    html = await response.text()
                    # Use run_in_executor for BeautifulSoup parsing as it's CPU-bound
                    loop = asyncio.get_running_loop()
                    return await loop.run_in_executor(None, parse_audio_url, html)
    except Exception as e:
        print(f"Error getting audio url async: {e}")
    return {"audio_url": None, "canonical_word": None}

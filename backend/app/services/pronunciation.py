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
    """Parse HTML to extract audio URL"""
    soup = BeautifulSoup(html, "html.parser")
    
    # Try the original method first
    div = soup.find("h1", class_="mdc-typography--headline4 ltr d-inline position-relative")
    
    if div and div.find("small") and "data-url" in div.find("small").attrs:
        audio_link = div.find("small")["data-url"]
        return audio_link
        
    # Alternative method - look for any audio element
    audio_elements = soup.find_all("audio")
    for audio in audio_elements:
        if audio.has_attr("src"):
            return audio["src"]
            
    # Try to find any element with data-url attribute
    elements_with_data_url = soup.find_all(attrs={"data-url": True})
    if elements_with_data_url:
        audio_link = elements_with_data_url[0]["data-url"]
        return audio_link
    
    return None

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
    return None

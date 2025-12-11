import aiohttp
import asyncio
from typing import List

async def get_synonyms_async(word: str) -> List[str]:
    """
    Fetches synonyms for a German word using the OpenThesaurus API.
    Returns a list of synonyms.
    """
    url = f"https://www.openthesaurus.de/synonyme/search?q={word}&format=application/json"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    synonyms = []
                    # OpenThesaurus returns a list of "synsets"
                    if "synsets" in data:
                        for synset in data["synsets"]:
                            for term in synset.get("terms", []):
                                term_text = term.get("term")
                                # Avoid adding the word itself to its synonyms list
                                if term_text and term_text.lower() != word.lower():
                                    synonyms.append(term_text)
                    
                    # Deduplicate and limit to top 10 to avoid overwhelming UI
                    return list(dict.fromkeys(synonyms))[:10]
    except Exception as e:
        print(f"Error fetching synonyms: {e}")
        return []
    
    return []

import asyncio
from deep_translator import GoogleTranslator

async def get_persian_definition_async(text: str) -> list[str]:
    """
    Get Persian definition/translation using Google Translate.
    Returns a list of strings to maintain compatibility.
    """
    try:
        loop = asyncio.get_running_loop()
        def _translate():
            translator = GoogleTranslator(source='de', target='fa')
            return translator.translate(text)
        
        result = await loop.run_in_executor(None, _translate)
        return [result] if result else []
    except Exception as e:
        print(f"Error translating to Persian: {e}")
        return []


async def translate_text_async(text: str, source: str = 'de', target: str = 'en') -> str:
    """
    Generic async translation using GoogleTranslator (deep-translator).
    """
    try:
        loop = asyncio.get_running_loop()
        def _translate():
            translator = GoogleTranslator(source=source, target=target)
            return translator.translate(text)
        
        result = await loop.run_in_executor(None, _translate)
        return result if result else ""
    except Exception as e:
        print(f"Error translating to {target}: {e}")
        return ""

async def get_word_with_article_async(german_word: str) -> str:
    """
    Attempts to find the German article (der/die/das) by:
    1. Translating DE -> EN (Haus -> House)
    2. Translating EN "the House" -> DE "das Haus"
    """
    try:
        # Step 1: Translate to English
        # We could reuse the other translation if we coordinated, but for simplicity/speed we just do it here.
        # It's fast enough.
        loop = asyncio.get_running_loop()
        
        def _get_article_logic():
            de_translator = GoogleTranslator(source='de', target='en')
            en_word = de_translator.translate(german_word)
            
            if not en_word:
                return None

            # Clean English word (remove a/an/the)
            en_clean = en_word.lower()
            for prefix in ["a ", "an ", "the "]:
                if en_clean.startswith(prefix):
                    en_clean = en_clean[len(prefix):]
            
            # Step 2: Translate back with "the"
            en_translator = GoogleTranslator(source='en', target='de')
            gendered = en_translator.translate(f"the {en_clean}")
            
            # Additional Cleanup: Sometimes it returns "das House" (mixed) or "das ein X"
            # We only want basic articles.
            if gendered:
                 # Check common issue "das ein Haus"
                 gendered = gendered.replace(" das ein ", " das ").replace(" der ein ", " der ").replace(" die eine ", " die ")
                 # Or simply looks like "das ein Haus" at start
                 if gendered.lower().startswith("das ein "):
                     gendered = "das " + gendered[8:]
                 elif gendered.lower().startswith("der ein "):
                     gendered = "der " + gendered[8:]
                 elif gendered.lower().startswith("die eine "):
                     gendered = "die " + gendered[9:]

            return gendered

        candidate = await loop.run_in_executor(None, _get_article_logic)

        if candidate and german_word.lower() in candidate.lower():
             return candidate
             
    except Exception as e:
        print(f"Error determining article: {e}")
    
    return german_word

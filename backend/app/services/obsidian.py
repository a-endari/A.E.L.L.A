import io
import zipfile
import aiohttp
import asyncio
from typing import List, Dict, Any

async def create_obsidian_zip(cards: List[Dict[str, Any]]) -> io.BytesIO:
    """
    Generates a ZIP file compatible with Obsidian.
    Contains:
    1. Words.md (The main note)
    2. README.md (Instructions)
    3. Media/ (Folder with MP3s)
    """
    zip_buffer = io.BytesIO()
    
    words_md_content = "# My Vocabulary\n\n"
    readme_content = """# Obsidian Export Guide

1.  **Extract** this zip file.
2.  Copy `Words.md` and the `Media` folder into your Obsidian Vault.
3.  **Important**: Ensure Obsidian can see the media files.
    -   Go to **Settings > Files & Links**.
    -   Check "Default location for new attachments". If it's "Same folder as current file" or "In subfolder under current folder", you are good to go if you keep the structure.
    -   Ideally, just drag the `Media` folder into your vault.
    
## Callouts
This note uses Obsidian Callouts (e.g., `> [!NOTE]`). They are supported natively in recent Obsidian versions.
"""

    async with aiohttp.ClientSession() as session:
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            # Add README
            zf.writestr("README.md", readme_content)
            
            # Process cards
            for card in cards:
                clean_word = card.get('clean_word', 'Unknown')
                # Handle list of definitions
                definitions = card.get('definitions', [])
                if isinstance(definitions, str):
                    definitions = [definitions]
                definition_text = "\n".join([f"- {d}" for d in definitions])
                
                english = card.get('english_definition', '')
                synonyms = ", ".join(card.get('synonyms', []))
                audio_url = card.get('audio_url')
                
                # Append to Words.md
                words_md_content += f"## {clean_word}\n"
                
                if audio_url:
                    filename = f"{clean_word}.mp3"
                    # Add audio link (Obsidian format)
                    words_md_content += f"![[{filename}]]\n\n"
                    
                    # Download and add to zip
                    try:
                        async with session.get(audio_url) as resp:
                            if resp.status == 200:
                                audio_data = await resp.read()
                                zf.writestr(f"Media/{filename}", audio_data)
                    except Exception as e:
                        print(f"Failed to download audio for {clean_word}: {e}")
                
                words_md_content += f"**English**: {english}  \n"
                words_md_content += f"**Persian**:\n{definition_text}  \n"
                
                if synonyms:
                    words_md_content += f"\n> [!NOTE] Synonyms\n> {synonyms}\n"
                
                words_md_content += "\n---\n\n"

            # Add Words.md
            zf.writestr("Words.md", words_md_content)

    zip_buffer.seek(0)
    return zip_buffer

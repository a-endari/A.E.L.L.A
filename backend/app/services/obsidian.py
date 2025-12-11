import io
import zipfile
import aiohttp
import asyncio
from typing import List, Dict, Any

async def create_obsidian_zip(cards: List[Dict[str, Any]], note_name: str = "My Vocabulary") -> io.BytesIO:
    """
    Generates a ZIP file compatible with Obsidian.
    Contains:
    1. {NoteName}.md (The main note)
    2. README.md (Instructions)
    3. Media/ (Folder with MP3s)
    """
    zip_buffer = io.BytesIO()
    
    # Use Title Case for the header and filename
    # e.g. "german verbs" -> "German Verbs"
    # Note: .title() can be basic, but usually sufficient.
    display_title = note_name.title()
    
    words_md_content = f"# {display_title}\n\n"
    readme_content = """# Obsidian Export Guide

1.  **Extract** this zip file.
1.  **Extract** this zip file.
2.  Copy the markdown file (e.g. `German Verbs.md`) and the `Media` folder into your Obsidian Vault.
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
                
                # Append to Words.md (Callout Format)
                # Note: 'tldr' is a common callout type, '-' makes it collapsible (collapsed by default)
                words_md_content += f"> [!tldr]- {clean_word}\n"
                
                if audio_url:
                    filename = f"{clean_word}.mp3"
                    words_md_content += f"> ![[{filename}]]\n"
                    
                    # Download and add to zip
                    try:
                        async with session.get(audio_url) as resp:
                            if resp.status == 200:
                                audio_data = await resp.read()
                                zf.writestr(f"Media/{filename}", audio_data)
                    except Exception as e:
                        print(f"Failed to download audio for {clean_word}: {e}")
                
                words_md_content += "> ---\n"
                words_md_content += f"> **English**: {english}\n"
                words_md_content += "> ---\n"
                
                # Handle multi-line Persian definitions inside the quote block
                if definition_text:
                    formatted_persian = definition_text.replace('\n', '\n> ')
                    words_md_content += f"> **فارسی**:\n> {formatted_persian}\n"
                
                words_md_content += "> ---\n"
                
                if synonyms:
                     words_md_content += f"> **Synonyms**: {synonyms}\n"
                
                words_md_content += "\n"

            # Add Main Note
            zf.writestr(f"{display_title}.md", words_md_content)

    zip_buffer.seek(0)
    return zip_buffer

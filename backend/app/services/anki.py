import genanki
import random
from typing import List, Dict, Any
from io import BytesIO

def create_deck(cards_data: List[Dict[str, Any]], deck_name: str = 'Universal Language Deck') -> BytesIO:
    """
    Generates an Anki deck (.apkg) from a list of word data objects.
    Returns: BytesIO object containing the .apkg file content.
    """
    # Unique Deck ID (random but consistent for this session)
    deck_id = random.randrange(1 << 30, 1 << 31)
    
    # CSS for the card
    style = """
    .card {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
     font-size: 20px;
     text-align: center;
     color: #0f172a; /* Slate 900 */
     background-color: #f8fafc; /* Slate 50 */
     height: 100vh;
     display: flex;
     flex-direction: column;
     justify-content: center;
     align-items: center;
     margin: 0;
     padding: 20px;
     box-sizing: border-box;
    }

    .container {
      background: #ffffff;
      border-radius: 16px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      padding: 40px;
      width: 100%;
      max-width: 600px;
      border: 1px solid #e2e8f0;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .label {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #a855f7; /* Purple 500 */
      font-weight: 600;
      margin-bottom: 4px;
    }

    .word {
      font-size: 2.5rem;
      font-weight: 800;
      color: #1e293b; /* Slate 800 */
      margin: 0;
    }

    .definition {
      font-size: 1.25rem;
      color: #334155; /* Slate 700 */
      font-style: italic;
      line-height: 1.6;
    }

    .persian {
      font-size: 1.25rem;
      color: #475569; /* Slate 600 */
      direction: rtl;
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px dashed #cbd5e1;
    }

    .synonyms {
      font-size: 0.875rem;
      color: #64748b; /* Slate 500 */
      margin-top: 12px;
      background: #f1f5f9;
      padding: 8px 12px;
      border-radius: 8px;
    }

    .divider {
      border: 0;
      height: 1px;
      background: #e2e8f0;
      margin: 20px 0;
      width: 100%;
    }

    .footer {
      margin-top: 30px;
      font-size: 0.75rem;
      color: #94a3b8;
    }

    a {
      color: #a855f7;
      text-decoration: none;
      font-weight: 500;
    }

    /* Dark Mode (Anki Mobile / Desktop Night Mode) */
    .nightMode .card {
      background-color: #020617; /* Slate 950 */
      color: #e2e8f0;
    }
    
    .nightMode .container {
      background: #0f172a; /* Slate 900 */
      border-color: #1e293b;
      box-shadow: none;
    }

    .nightMode .word { color: #f8fafc; }
    .nightMode .definition { color: #cbd5e1; }
    .nightMode .persian { color: #94a3b8; border-color: #334155; }
    .nightMode .synonyms { background: #1e293b; color: #94a3b8; }
    .nightMode .divider { background: #1e293b; }
    """

    # Define the Model (Note Type)
    model = genanki.Model(
        1607392319,
        'Universal Language App Model',
        fields=[
            {'name': 'German'},
            {'name': 'English'},
            {'name': 'Persian'},
            {'name': 'Synonyms'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': """
                <div class="container">
                  <div class="label">GERMAN</div>
                  <div class="word">{{German}}</div>
                </div>
                <div class="footer">
                   Created with <a href="https://github.com/a-endari/A.E.L.L.A.">A.E.L.L.A.</a>
                </div>
                """,
                'afmt': """
                <div class="container">
                  <div class="label">GERMAN</div>
                  <div class="word">{{German}}</div>
                  
                  <div class="divider"></div>
                  
                  <div class="label">ENGLISH</div>
                  <div class="definition">{{English}}</div>

                  {{#Persian}}
                  <div class="persian">{{Persian}}</div>
                  {{/Persian}}

                  {{#Synonyms}}
                  <div class="synonyms">syn: {{Synonyms}}</div>
                  {{/Synonyms}}
                </div>
                <div class="footer">
                   Created with <a href="https://github.com/a-endari/A.E.L.L.A.">A.E.L.L.A.</a>
                </div>
                """,
            },
        ],
        css=style)

    deck = genanki.Deck(deck_id, deck_name)

    for card in cards_data:
        german = card.get('clean_word', '')
        english = card.get('english_definition', '')
        
        # Handle list of definitions
        definitions = card.get('definitions', [])
        if isinstance(definitions, str):
            definitions = [definitions]
        persian = "<br>".join([f"{i+1}. {d}" for i, d in enumerate(definitions)])
        synonyms = ", ".join(card.get('synonyms', []))
        
        note = genanki.Note(
            model=model,
            fields=[german, english, persian, synonyms]
        )
        deck.add_note(note)

    # Write to BytesIO
    out = BytesIO()
    package = genanki.Package(deck)
    package.write_to_file(out)
    out.seek(0)
    
    return out

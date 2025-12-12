# 🏗️ Architecture Overview

Technical documentation for developers working on A.E.L.L.A.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Browser                         │
│                     (localhost:3000)                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  App Router │  │  Components │  │   Themes    │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP (REST API)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend (FastAPI)                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  API Routes │  │   Services  │  │   Database  │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  SQLite  │   │ Edge TTS │   │  Google  │
        │ Database │   │  (Audio) │   │Translate │
        └──────────┘   └──────────┘   └──────────┘
```

---

## Frontend Architecture

### Tech Stack
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: CSS Modules + CSS Custom Properties
- **HTTP Client**: Axios
- **Animations**: Framer Motion

### Directory Structure
```
frontend/
├── app/
│   ├── layout.tsx       # Root layout with theme provider
│   ├── page.tsx         # Main application page
│   └── globals.css      # Global styles and CSS variables
├── components/          # Reusable UI components
├── public/
│   └── themes/          # Theme CSS files
└── next.config.ts       # Next.js configuration
```

### State Management
- Local React state with `useState`
- No external state library (app is simple enough)
- Theme state persisted in `localStorage`

### Theming System
Themes use CSS custom properties defined in separate files:
```css
/* Example theme structure */
:root[data-theme="midnight"] {
  --bg-primary: #1a1a2e;
  --text-primary: #eaeaea;
  --accent: #7c3aed;
}
```

---

## Backend Architecture

### Tech Stack
- **Framework**: FastAPI (Python 3.10+)
- **Database**: SQLite with raw SQL
- **TTS**: Microsoft Edge TTS (edge-tts library)
- **Translation**: Google Translate (googletrans)

### Directory Structure
```
backend/
├── main.py              # FastAPI app and routes
├── database.py          # Database operations
├── requirements.txt     # Python dependencies
├── static/
│   └── audio/           # Cached TTS audio files
└── vocabulary.db        # SQLite database (auto-created)
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/lists` | Get all vocabulary lists |
| POST | `/api/lists` | Create new list |
| DELETE | `/api/lists/{id}` | Delete a list |
| GET | `/api/lists/{id}/cards` | Get cards in a list |
| POST | `/api/lists/{id}/cards` | Add card to list |
| DELETE | `/api/lists/{id}/cards/{word}` | Remove card |
| POST | `/api/lookup` | Look up a word |
| POST | `/api/anki/download` | Export list to Anki |
| POST | `/api/obsidian/download` | Export list to Obsidian |

### Database Schema

```sql
-- Lists table
CREATE TABLE lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cards table
CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    word TEXT NOT NULL,
    data JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (list_id) REFERENCES lists(id) ON DELETE CASCADE
);
```

---

## Data Flow

### Word Lookup Flow
```
1. User enters word → Frontend
2. POST /api/lookup → Backend
3. Fetch definition from Google Translate
4. Generate TTS audio (if not cached)
5. Return combined data → Frontend
6. Display results to user
```

### Export Flow (Anki)
```
1. User clicks "Export to Anki" → Frontend
2. POST /api/anki/download with card data → Backend
3. Generate .apkg file with genanki
4. Return file as download → Frontend
5. Browser downloads file
```

---

## External Services

| Service | Purpose | Rate Limiting |
|---------|---------|---------------|
| **Google Translate** | Definitions, translations | ~100 req/hour (unofficial) |
| **Microsoft Edge TTS** | Audio pronunciation | No hard limit (free) |

### Caching Strategy
- Audio files are cached in `backend/static/audio/`
- Cached by word hash to avoid duplicates
- Cleanup job removes unused audio on startup

---

## Docker Architecture

```yaml
services:
  backend:   # Python/FastAPI container
    - Port 8000
    - Volume: ./backend:/app (dev mode)
    
  frontend:  # Node.js/Next.js container
    - Port 3000
    - Volume: ./frontend:/app (dev mode)
    - Depends on: backend
```

### Network
- Docker creates internal network `universallanguageapp_default`
- Frontend connects to backend via `http://backend:8000`
- Both services exposed to host on their respective ports

---

## Security Considerations

- No authentication (local-only app)
- CORS configured for localhost only
- No sensitive data storage
- All external API calls are read-only

---

## Performance

- Frontend uses Next.js static optimization where possible
- Backend uses async/await for non-blocking I/O
- Audio files cached to reduce TTS calls
- SQLite is sufficient for single-user local app

# 🌐 Universal Language App (Project A.E.L.L.A.)

> **A.E.L.L.A.** — *All Encapsulated Language Learning Assistant* (or *Abbas Endari Language Learning Assistant😉*)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Backend-FastAPI-blue?logo=python&logoColor=white)
![Next.js](https://img.shields.io/badge/Frontend-Next.js_14-black?logo=next.js&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

A scalable, comprehensive language learning companion designed to be your **Personal Language Pal**. Built to assist with vocabulary acquisition, pronunciation mastery, and knowledge retention through seamless integration with powerful tools like **Anki** and **Obsidian**.

---

## ✨ Features (Planned & In-Progress)

- 🗣️ **Instant Pronunciation**: High-quality audio fetching for words you learn.
- 📖 **Smart Definitions**: Auto-retrieval of definitions, cleaning out noise.
- 🧠 **Space Repetition Ready**: Auto-generate formatted **Anki** flashcards.
- 📝 **Knowledge Graph**: Export entries to **Obsidian** markdown with rich metadata.
- 🚀 **Offline Capable**: Designed to run locally on your Mac/PC.

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: [Next.js](https://nextjs.org/) (React)
- **Styling**: Vanilla CSS / Modules (Premium Aesthetic)
- **Deployment**: Static Export (GitHub Pages compatible)

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Concurrency**: Fully Async fetching
- **Hosting**: PythonAnywhere compatible

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to start learning!

---

## 🔮 Future Roadmap

- [ ] **Electron Integration**: Bundle as a standalone desktop executable.
- [ ] **Flashcard Generator**: One-click `.apkg` export.
- [ ] **Polyglot Mode**: Support for multi-language dictionaries.
- [ ] **AI Context**: LLM-powered sentence generation for vocab words.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by <strong>Abbas Endari</strong>
</p>

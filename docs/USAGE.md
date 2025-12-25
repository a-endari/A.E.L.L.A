# 📖 Usage Guide

Learn how to use AELLA effectively.

---

## Getting Started

After [installing](INSTALLATION.md) and starting the app, open your browser to:

- **<http://localhost:3000>** (default)

---

## Core Features

### 🔍 Word Lookup

The main feature of AELLA is looking up German words and getting comprehensive information.

**How to use**:

1. Type a German word in the search box
2. Press Enter or click the search button
3. View the results including:
   - **Clean word**: The standardized form
   - **Definitions**: In English and Persian
   - **Pronunciation**: Click to hear the word
   - **Examples**: Usage in context

### 📝 Vocabulary Lists

Organize your learning with custom vocabulary lists.

**Creating a List**:

1. Click the "+" button in the sidebar
2. Enter a name for your list
3. Click Create

**Adding Words to a List**:

1. Search for a word
2. Click "Save" to add it to the currently active list

**Switching Lists**:

1. Click on any list in the sidebar to make it active
2. The active list is highlighted

**Deleting a List**:

1. Select the list
2. Click the delete button
3. Confirm deletion

### 🧠 Anki Export

Export your vocabulary to [Anki](https://apps.ankiweb.net/) for spaced repetition learning.

**How to export**:

1. Select a vocabulary list
2. Click "Export to Anki"
3. A `.apkg` file will download
4. Open Anki and import the file

**Card Format**:

- **Front**: German word with pronunciation
- **Back**: Definitions in English and Persian, examples

### 📓 Obsidian Export

Export your vocabulary to [Obsidian](https://obsidian.md/) for knowledge management.

**How to export**:

1. Select a vocabulary list
2. Click "Export to Obsidian"
3. A `.md` file will download
4. Move the file to your Obsidian vault

**Note Format**:

- Structured with YAML frontmatter
- Includes all word data
- Uses collapsible callouts for organization

---

## Interface Overview

### Sidebar (Left)

- 📚 **Vocabulary Lists**: All your saved lists
- ➕ **Add List**: Create new list button
- 🎨 **Theme Selector**: Switch between visual themes

### Main Area (Center)

- 🔍 **Search Bar**: Enter words to look up
- 📋 **Results Panel**: View word information
- 💾 **Save Button**: Add word to current list

### Controls (Right/Top)

- 📤 **Export Buttons**: Anki and Obsidian export
- 🗑️ **Delete**: Remove current list

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Search for the entered word |
| `Esc` | Clear the search box |

---

## Themes

AELLA comes with multiple beautiful themes:

| Theme | Description |
|-------|-------------|
| **Midnight** | Dark theme with purple accents (default) |
| **Paper** | Light, clean, minimal theme |
| **Tokyo Night** | Dark theme with blue accents |
| **Ayu Mirage** | Warm dark theme |

**Changing Themes**:

1. Click the theme selector in the sidebar
2. Choose your preferred theme
3. Theme is saved automatically

---

## Tips & Best Practices

### Learning Workflow

1. **Start a Session**: Create a new list for today's learning
2. **Explore Words**: Look up words you encounter while reading/studying
3. **Save Important Ones**: Add words you want to remember
4. **Export to Anki**: At the end of the session, export to Anki
5. **Review Daily**: Use Anki's spaced repetition

### Organizing Lists

- 📅 **By Date**: "December 2024 Vocabulary"
- 📖 **By Source**: "Harry Potter Book 1"
- 🎯 **By Topic**: "Kitchen Vocabulary"
- 📊 **By Level**: "A1 Basics", "B2 Advanced"

### Pronunciation Practice

1. Look up a word
2. Click the pronunciation button
3. Listen carefully
4. Repeat out loud
5. Click again and compare

---

## Troubleshooting

### "Failed to fetch" Error

The backend server is not running.

**Solutions**:

- If using Docker: Check that containers are running with `docker ps`
- If manual: Ensure the backend is running on port 8000

### No Audio Playing

Audio file might not be available.

**Solutions**:

- Check your browser's volume
- Try a different word
- Some rare words may not have audio

### Slow Search Results

The API may be fetching from external sources.

**Solutions**:

- First searches are slower (caching happens)
- Subsequent searches for the same word will be faster

---

## Data Storage

- **Vocabulary Lists**: Stored in the backend database
- **Audio Files**: Cached locally in `backend/static/audio/`
- **User Preferences**: Stored in browser local storage

---

## Next Steps

- 📦 Having issues? Check the [Installation Guide](INSTALLATION.md)
- 🤝 Want to contribute? Read the [Contributing Guidelines](CONTRIBUTING.md)
- 🐛 Found a bug? [Open an issue](https://github.com/a-endari/A.E.L.L.A/issues)

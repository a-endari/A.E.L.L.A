# 🤝 Contributing Guidelines

Thank you for your interest in contributing to A.E.L.L.A.! This document outlines the standards and processes for contributing to the project.

---

## Code of Conduct

By participating in this project, you agree to maintain a welcoming, inclusive environment. Be respectful, constructive, and patient with others.

---

## How to Contribute

### 🐛 Reporting Bugs

1. **Search existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Docker version, browser)
   - Screenshots if applicable

### ✨ Suggesting Features

1. **Search existing issues** to see if it's already suggested
2. **Create a feature request** with:
   - Clear description of the feature
   - Why it would be useful
   - Possible implementation approach (optional)

### 📝 Improving Documentation

Documentation improvements are always welcome! This includes:
- Fixing typos
- Clarifying instructions
- Adding examples
- Translating docs

### 💻 Contributing Code

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following our coding standards
4. **Test thoroughly**
5. **Submit a Pull Request**

---

## Development Setup

Follow the [Installation Guide](INSTALLATION.md) for local setup.

### Project Structure

```
UniversalLanguageApp/
├── backend/          # Python FastAPI server
│   ├── main.py       # Entry point
│   ├── database.py   # Database operations
│   └── static/       # Static files (audio, etc.)
├── frontend/         # Next.js React application
│   ├── app/          # Next.js App Router pages
│   └── public/       # Static assets
├── docs/             # Documentation
├── docker-compose.yml
└── README.md
```

---

## Coding Standards

### Python (Backend)

**Style**:
- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints
- Maximum line length: 100 characters

**Naming Conventions**:
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants

**Example**:
```python
from typing import Optional

async def fetch_word_definition(word: str) -> Optional[dict]:
    """
    Fetch the definition of a German word.
    
    Args:
        word: The German word to look up.
        
    Returns:
        Dictionary containing word data, or None if not found.
    """
    clean_word = word.strip().lower()
    # Implementation...
    return result
```

### TypeScript/React (Frontend)

**Style**:
- Use TypeScript for all new code
- Functional components with hooks
- Use CSS Modules for styling

**Naming Conventions**:
- `camelCase` for functions and variables
- `PascalCase` for components and types
- File names should match component names

**Example**:
```typescript
interface WordCardProps {
  word: string;
  definition: string;
  onSave: () => void;
}

export function WordCard({ word, definition, onSave }: WordCardProps) {
  const handleClick = () => {
    onSave();
  };

  return (
    <div className={styles.card}>
      <h3>{word}</h3>
      <p>{definition}</p>
      <button onClick={handleClick}>Save</button>
    </div>
  );
}
```

### CSS

**Style**:
- Use CSS Modules (`.module.css`)
- Use CSS custom properties for theming
- Mobile-first responsive design

**Naming Conventions**:
- `camelCase` for class names in CSS Modules
- Descriptive, component-scoped names

---

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(frontend): add dark mode theme support

fix(backend): handle empty word input gracefully

docs: update installation instructions for Windows

refactor(api): simplify word lookup endpoint
```

---

## Pull Request Process

### Before Submitting

- [ ] Code follows project standards
- [ ] All tests pass
- [ ] Documentation is updated (if needed)
- [ ] Commit messages follow conventions
- [ ] PR description explains the changes

### PR Template

When creating a PR, include:

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactoring

## Testing
[How was this tested?]

## Screenshots (if applicable)
[Add screenshots for UI changes]
```

### Review Process

1. At least one maintainer must approve
2. All CI checks must pass
3. Requested changes must be addressed
4. PR will be squash-merged

---

## Testing

### Backend

```bash
cd backend
pytest
```

### Frontend

```bash
cd frontend
npm run lint
npm run build  # Ensures no build errors
```

---

## Questions?

- 📬 Open an issue for general questions
- 💬 Tag maintainers for urgent matters

---

## Recognition

All contributors will be recognized in the README. Thank you for helping make A.E.L.L.A. better! 🎉

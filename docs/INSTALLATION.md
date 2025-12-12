# 📦 Installation Guide

Complete installation instructions for A.E.L.L.A. (Universal Language App).

## Prerequisites

Before installing, ensure you have one of the following:

| Method | Requirements |
|--------|--------------|
| 🐳 **Docker** (Recommended) | [Docker Desktop](https://docs.docker.com/get-docker/) |
| 🛠️ **Manual Setup** | Python 3.10+, Node.js 18+ |

---

## Option 1: Docker Installation (Recommended)

The fastest way to get started. No need to install Python or Node.js.

### Step 1: Install Docker Desktop

Download and install [Docker Desktop](https://docs.docker.com/get-docker/) for your operating system:
- **macOS**: [Download](https://docs.docker.com/desktop/install/mac-install/)
- **Windows**: [Download](https://docs.docker.com/desktop/install/windows-install/) (requires WSL2)
- **Linux**: [Download](https://docs.docker.com/desktop/install/linux-install/)

### Step 2: Clone the Repository

```bash
git clone https://github.com/a-endari/A.E.L.L.A.git
cd A.E.L.L.A
```

### Step 3: Start the Application

```bash
docker-compose up --build
```

### Step 4: Access the App

| Service | URL |
|---------|-----|
| **Frontend (App)** | http://localhost:3000 |
| **Backend API** | http://localhost:8000 |
| **API Docs** | http://localhost:8000/docs |

### Stopping the Application

Press `Ctrl+C` in the terminal, then:
```bash
docker-compose down
```

> 📖 For advanced Docker usage and troubleshooting, see [DOCKER.md](DOCKER.md)

---

## Option 2: Manual Installation

For developers who want to modify the code or don't want to use Docker.

### Step 1: Clone the Repository

```bash
git clone https://github.com/a-endari/A.E.L.L.A.git
cd A.E.L.L.A
```

### Step 2: Backend Setup (Python/FastAPI)

**Requirements**: Python 3.10 or higher

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn main:app --reload
```

The API will be running at `http://localhost:8000`

### Step 3: Frontend Setup (Node.js/Next.js)

Open a **new terminal** window.

**Requirements**: Node.js 18 or higher

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be running at `http://localhost:3000`

### Step 4: Access the App

Open your browser and go to `http://localhost:3000`

---

## Verifying Installation

After starting the app, verify everything works:

1. ✅ **Frontend loads**: Visit http://localhost:3000 and see the UI
2. ✅ **Backend responds**: Visit http://localhost:8000/docs and see the API documentation
3. ✅ **Connection works**: Search for a word in the app and verify results appear

---

## Common Issues

### Docker: "Port already in use"

Another application is using port 3000 or 8000.

**Solution**: Change ports in `docker-compose.yml`:
```yaml
ports:
  - "3001:3000"  # Change frontend port
  - "8001:8000"  # Change backend port
```

### Docker: "Cannot connect to Docker daemon"

Docker Desktop is not running.

**Solution**: Start Docker Desktop application.

### Manual: "python not found" or "node not found"

Python or Node.js is not installed or not in PATH.

**Solution**: Install from official websites:
- Python: https://python.org/downloads/
- Node.js: https://nodejs.org/

### Manual: "Module not found" errors

Dependencies are not installed.

**Solution**: Run `pip install -r requirements.txt` (backend) or `npm install` (frontend).

---

## Updating

To get the latest version:

```bash
# Pull latest changes
git pull origin main

# If using Docker
docker-compose up --build

# If using manual setup
# Backend:
cd backend && pip install -r requirements.txt
# Frontend:
cd frontend && npm install
```

---

## Uninstalling

### Docker Method

```bash
# Stop and remove containers
docker-compose down -v

# Remove images (optional)
docker rmi aella-frontend aella-backend

# Delete repository folder
cd .. && rm -rf A.E.L.L.A
```

### Manual Method

```bash
# Just delete the repository folder
cd .. && rm -rf A.E.L.L.A
```

---

## Next Steps

- 📖 Read the [Usage Guide](USAGE.md) to learn how to use the app
- 🤝 Check [Contributing Guidelines](CONTRIBUTING.md) if you want to help develop the app

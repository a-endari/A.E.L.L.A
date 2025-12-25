# 🐳 Docker Quick Start

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

## Option 1: Use Pre-built Images (Fastest)

Pull and run pre-built images from GitHub Container Registry:

```bash
# Clone the repository
git clone https://github.com/a-endari/A.E.L.L.A.git
cd A.E.L.L.A

# Run using pre-built images
docker-compose -f docker-compose.ghcr.yml up
```

This downloads ready-to-use images (~500MB) and starts immediately!

---

## Option 2: Build Locally

Build the images yourself (takes 5-10 minutes first time):

```bash
git clone https://github.com/a-endari/A.E.L.L.A.git
cd A.E.L.L.A
docker-compose up --build
```

---

## Running with Docker

1. **Start the application**

   ```bash
   docker-compose up
   ```

2. **Access the app**
   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000>
   - API Docs: <http://localhost:8000/docs>

## Development Mode

The Docker setup includes hot-reloading for both frontend and backend:

- **Backend**: Automatically reloads on Python file changes
- **Frontend**: Automatically rebuilds on React/Next.js file changes

## Stopping the Application

```bash
# Stop containers (Ctrl+C in the terminal, then:)
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

## Rebuilding After Changes

```bash
# Rebuild containers after dependency changes
docker-compose up --build
```

## Troubleshooting

**Port already in use?**

```bash
# Change ports in docker-compose.yml
# Frontend: "3001:3000" instead of "3000:3000"
# Backend: "8001:8000" instead of "8000:8000"
```

**Containers won't start?**

```bash
# Clean rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

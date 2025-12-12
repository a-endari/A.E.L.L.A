# 🐳 Docker Quick Start

## Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

## Running with Docker

1. **Clone the repository**
   ```bash
   git clone &lt;your-repo-url&gt;
   cd UniversalLanguageApp
   ```

2. **Start the application**
   ```bash
   docker-compose up
   ```

3. **Access the app**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

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

# Development Setup

This guide is for developers who want to modify the source code or run the application in "Web Mode" via Docker.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- **OR** Python 3.10+ and Node.js 20+ for local manual setup.

## Running with Docker (Web Mode)

The easiest way to develop the web version.

```bash
docker-compose up --build
```

Access the app at `http://localhost:3000`.

## Local Desktop Development (Electron)

To develop the desktop application:

1. **Setup Environment**:

    ```bash
    ./setup_mac_linux.sh
    # OR
    setup_windows.bat
    ```

2. **Run**:

    ```bash
    npm run dev
    ```

## Project Structure

- `backend/`: FastAPI Python server.
- `frontend/`: Next.js React application.
- `electron/`: Electron main process logic.

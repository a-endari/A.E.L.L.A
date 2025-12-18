@echo off
setlocal
echo 🚀 Setting up Universal Language App...

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: Check for Node.js
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed or not in PATH.
    pause
    exit /b 1
)

:: Backend Setup
echo 📦 Setting up Backend...
if not exist .venv (
    python -m venv .venv
)
call .venv\Scripts\activate.bat
pip install -r backend\requirements.txt

:: Frontend Setup
echo 📦 Setting up Frontend...
cd frontend
call npm install
cd ..

echo ✅ Setup Complete!
echo.
set /p runNow="🚀 Do you want to run the app now? (Y/N) "
if /i "%runNow%"=="Y" (
    echo Starting Backend and Frontend...
    start "Universal Backend" cmd /k "call .venv\Scripts\activate.bat && cd backend && uvicorn main:app --reload"
    start "Universal Frontend" cmd /k "cd frontend && npm run dev"
    echo Servers started in new windows!
) else (
    echo To run manually:
    echo --------------------------------
    echo 1. Start Backend (Terminal 1):
    echo    .venv\Scripts\activate
    echo    cd backend
    echo    uvicorn main:app --reload
    echo.
    echo 2. Start Frontend (Terminal 2):
    echo    cd frontend
    echo    npm run dev
    echo --------------------------------
)
pause

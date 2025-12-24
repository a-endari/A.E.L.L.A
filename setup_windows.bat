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
echo 🚀 How would you like to run the app?
echo 1) Desktop App (Electron) - Recommended
echo 2) Web Environment (Next.js + Python server)
set /p choice="Enter choice [1]: "
if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    echo Starting Desktop App...
    npm run dev
) else (
    echo Starting Web Environment...
    start "Universal Backend" cmd /k "call .venv\Scripts\activate.bat && cd backend && uvicorn main:app --reload"
    start "Universal Frontend" cmd /k "cd frontend && npm run dev"
    echo Servers started in new windows!
)
pause

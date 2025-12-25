#!/bin/bash
set -e

echo "🚀 Setting up AELLA..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first."
    exit 1
fi

# Check for Node.js
if ! command -v npm &> /dev/null; then
    echo "❌ Node.js is not installed. Please install it first."
    exit 1
fi

# Backend Setup
echo "📦 Setting up Backend..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r backend/requirements.txt

# Frontend Setup
echo "📦 Setting up Frontend..."
cd frontend
npm install
cd ..

echo "✅ Setup Complete!"
echo ""
echo "🚀 How would you like to run the app?"
echo "1) Desktop App (Electron) - Recommended"
echo "2) Web Environment (Next.js + Python server)"
read -p "Enter choice [1]: " choice
choice=${choice:-1}

if [ "$choice" == "1" ]; then
    echo "Starting Desktop App..."
    npm run dev
else
    echo "Starting Web Environment..."
    # Background backend
    source .venv/bin/activate
    cd backend
    uvicorn main:app --reload > /dev/null 2>&1 &
    BACKEND_PID=$!
    echo "Backend started (PID: $BACKEND_PID)"
    
    cd ../frontend
    npm run dev &
    FRONTEND_PID=$!
    echo "Frontend started (PID: $FRONTEND_PID)"
    
    echo "Press any key to stop servers..."
    read -n 1
    
    kill $BACKEND_PID
    kill $FRONTEND_PID
    echo "Stopped."
fi


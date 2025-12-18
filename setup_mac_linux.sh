#!/bin/bash
set -e

echo "🚀 Setting up Universal Language App..."

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
read -p "🚀 Do you want to run the app now? (Y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Starting Backend and Frontend..."
    # Using osascript to open new tabs on standard Mac terminal or just backgrounding it (simpler)
    # Backgrounding is risky in simple script. Let's just print instructions for now or try to run.
    # User asked for "one command" to run.
    
    # Simple approach: Run backend in background, save PID, run frontend.
    source .venv/bin/activate
    cd backend
    uvicorn main:app --reload > /dev/null 2>&1 &
    BACKEND_PID=$!
    echo "Backend started (PID: $BACKEND_PID)"
    
    cd ../frontend
    npm run dev &
    FRONTEND_PID=$!
    echo "Frontend started (PID: $FRONTEND_PID)"
    
    echo "Press any key to stop servers and exit..."
    read -n 1
    
    kill $BACKEND_PID
    kill $FRONTEND_PID
    echo "Servers stopped."
else
    echo "To run manually:"
    echo "--------------------------------"
    echo "1. Start Backend (Terminal 1):"
    echo "   source .venv/bin/activate"
    echo "   cd backend"
    echo "   uvicorn main:app --reload"
    echo ""
    echo "2. Start Frontend (Terminal 2):"
    echo "   cd frontend"
    echo "   npm run dev"
    echo "--------------------------------"
fi

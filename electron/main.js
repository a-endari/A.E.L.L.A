const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const http = require('http');

let mainWindow;
let pythonProcess;

// Config
const PY_HOST = '127.0.0.1';
const PY_PORT = 8000;
const UI_PORT = 3000; // Dev mode port

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js'),
        },
        titleBarStyle: 'hiddenInset', // Mac style
    });

    const isDev = !app.isPackaged;

    if (isDev) {
        // Development: load from Next.js dev server
        const startUrl = process.env.ELECTRON_START_URL || `http://localhost:${UI_PORT}`;
        mainWindow.loadURL(startUrl);
    } else {
        // Production: load static files from 'out' directory
        mainWindow.loadFile(path.join(__dirname, '../out/index.html'));
    }

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

function startPythonBackend() {
    // Determine if we are running in dev or prod
    const isDev = !app.isPackaged;

    let scriptPath;
    let command;
    let args;

    if (isDev) {
        // Try to find local venv
        const venvPython = path.join(__dirname, '../.venv/bin/python');
        const fs = require('fs');

        if (fs.existsSync(venvPython)) {
            command = venvPython;
            console.log(`Using venv python: ${command}`);
        } else {
            command = 'python3'; // Fallback to system python
            console.log(`Using system python: ${command}`);
        }

        scriptPath = path.join(__dirname, '../backend/main.py');
        args = [scriptPath];
    } else {
        // In production, we expect an executable
        // This part requires PyInstaller logic which we will handle later.
        // For now, assuming packaged executable structure.
        scriptPath = path.join(process.resourcesPath, 'backend_dist', 'main');
        command = scriptPath;
        args = [];
        console.log(`Starting Python backend (Prod): ${command}`);
    }

    const cwd = isDev ? path.join(__dirname, '../backend') : app.getPath('userData');
    // Ensure userData dir exists
    if (!isDev) {
        const fs = require('fs');
        if (!fs.existsSync(cwd)) fs.mkdirSync(cwd, { recursive: true });
    }

    console.log(`Spawning Python in CWD: ${cwd}`);
    pythonProcess = spawn(command, args, { cwd });

    pythonProcess.stdout.on('data', (data) => {
        console.log(`[Python]: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`[Python API Error]: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

function exitPythonBackend() {
    if (pythonProcess) {
        pythonProcess.kill();
        pythonProcess = null;
    }
}

app.whenReady().then(() => {
    startPythonBackend();
    createWindow();

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});

app.on('will-quit', () => {
    exitPythonBackend();
});

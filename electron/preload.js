const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
    // Expose limited API if needed
    // For now, frontend calls localhost:8000 directly via axios
    // processInfo: process.versions
});

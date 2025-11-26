const { app, BrowserWindow } = require("electron/main");
const path = require("path");

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 300,
    height: 630,
    center: true,
    resizable: false,
    icon: path.join(__dirname, "assets/icons/heart_icon.png"), 
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
  });
  mainWindow.setMenuBarVisibility(false);

  const filePath = `build/index.html`;
  !app.isPackaged ? mainWindow.loadURL("http://localhost:5173") : mainWindow.loadFile(filePath);
  mainWindow.on("closed", () => (mainWindow = null));
  
}

app.whenReady().then(() => {
  createWindow();
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (mainWindow === null) {
    createWindow();
  }
});
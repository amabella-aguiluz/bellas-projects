const { app, BrowserWindow } = require("electron");
const path = require("path");

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 300,
    height: 630,
    center: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  if (!app.isPackaged) {
    mainWindow.loadURL("http://localhost:5173");
  } else {
    // load the packaged dist folder
    const indexPath = path.join(process.resourcesPath, "dist", "index.html");
    mainWindow.loadFile(indexPath);
  }

  mainWindow.setMenuBarVisibility(false);
  mainWindow.on("closed", () => (mainWindow = null));
}

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (mainWindow === null) createWindow();
});

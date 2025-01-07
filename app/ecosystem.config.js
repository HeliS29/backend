module.exports = {
  apps: [
    {
      name: "fastapi-app",                // Application name
      script: "uvicorn",                 // Uvicorn executable
      args: "main:app --host 0.0.0.0 --port 8000 &", // Your FastAPI app entrypoint
      exec_mode: "fork",                 // PM2 execution mode
      interpreter: "python3",            // Python interpreter
      autorestart: true,                 // Restart on failure
      watch: false,                      // Disable file watching
      max_memory_restart: "1G",          // Restart if memory usage exceeds 1GB
    },
  ],
};

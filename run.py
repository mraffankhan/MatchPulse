"""
MatchPulse: Resume-Job Matching System Runner
Starts the FastAPI web server on an available port (default: 8000).
"""

import socket
import sys
import webbrowser
import uvicorn


def find_available_port(start_port: int = 8000, max_attempts: int = 20) -> int:
    """Find the first open TCP port starting from start_port."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start_port


if __name__ == "__main__":
    host = "127.0.0.1"
    port = find_available_port(8000)

    print("\n" + "=" * 65)
    print(" 🚀 Launching MatchPulse: Resume–Job Matching System")
    print(f" 🌐 Web Dashboard: http://{host}:{port}")
    print(f" 📚 API Docs:      http://{host}:{port}/docs")
    print("=" * 65 + "\n")

    # Open web dashboard in default browser
    try:
        webbrowser.open(f"http://{host}:{port}")
    except Exception:
        pass

    uvicorn.run("backend.main:app", host=host, port=port, reload=False)

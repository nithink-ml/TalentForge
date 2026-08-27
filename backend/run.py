import os
import sys
from pathlib import Path
import uvicorn

ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT_DIR / "backend"

current_pythonpath = os.environ.get("PYTHONPATH", "")
paths_to_add = [str(ROOT_DIR), str(BACKEND_DIR)]
new_pythonpath = os.pathsep.join(paths_to_add + ([current_pythonpath] if current_pythonpath else []))
os.environ["PYTHONPATH"] = new_pythonpath

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        app_dir=str(ROOT_DIR),
    )

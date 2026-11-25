
from functools import wraps

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "data" / "activity.log"


def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        log = f"[LOG] {func.__name__} function called"

        print(log)

        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        with open(LOG_FILE, "a") as file:
            file.write(log + "\n")

        result = func(*args, **kwargs)

        return result

    return wrapper

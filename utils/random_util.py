from datetime import datetime
import random

def build_repo_name(prefix="repo-auto"):
    timetamp = datetime.now().strftime("%Y%m%d%H%M%S")
    stuffix = random.randint(100,999)
    return f"{prefix}-{timetamp}-{stuffix}"

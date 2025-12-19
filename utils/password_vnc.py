
from config import PATH_TO_VNC_PASSWORD_FILE


def get_password():
    with open(PATH_TO_VNC_PASSWORD_FILE, "r", encoding="utf-8") as f:
        password = f.read()
    return password.replace("\n", "").strip()

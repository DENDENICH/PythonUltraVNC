from pathlib import Path
from os import path
import sys


def _get_path_to_project():
    """Возвращает путь до папки проекта включая саму папку"""
    if getattr(sys, 'frozen', False):
        # Если скрипт был скомпилирован с помощью PyInstaller
        path_to_script = str(path.dirname(sys.executable))
        path_no_folder_dist = "/".join(path_to_script.split("\\")[:-1:])  # удаляем из пути папку dist, в которой находится .exe
        return Path(path_no_folder_dist)
    else:
        return Path(__file__).parent


PATH_TO_IPS_FILE = _get_path_to_project() / "data" / "ips.json"
PATH_TO_FAVORITE_FILE = _get_path_to_project() / "data" / "favorites.json"

PATH_TO_VNC = Path("C:/Program Files/uvnc bvba/UltraVNC/vncviewer.exe")
PATH_TO_VNC_PASSWORD_FILE = _get_path_to_project() / "data" / "vnc_password.txt"

import subprocess
import os

from config import PATH_TO_VNC, PATH_TO_VNC_PASSWORD_FILE
from errors import FileNotFound, OtherException
from .password_vnc import get_password


def connect_vnc(ip: str, port: str = "") -> None:
    """
    Подключение к vnc по ip
    :param ip: ip
    :param port: port
    :return: None
    """

    if port:
        connect_path = f"{ip}:{port}"
    else:
        connect_path = ip

    password = get_password()
    command = [
        PATH_TO_VNC,
        "-connect", connect_path,
        "-password", password
    ]
    print(command)
    try:
        # Запуск процесса
        subprocess.Popen(command)
    except FileNotFoundError:
        raise FileNotFound(f"Ошибка: Файл {PATH_TO_VNC} не найден. Проверьте путь к vncviewer.exe.")
    except Exception as e:
        raise OtherException(f"Произошла ошибка: {e}")

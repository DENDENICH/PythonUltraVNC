from typing import Dict, List
from pathlib import Path

from .base import UploadIPsBase
from .from_pdf import UploadIPsPDF
from .from_txt import UploadIPsText

from config import (
    PATH_TO_IPS_FILE
)
from errors import InvalidFormat


class UploadIPsManager:
    """
    Класс-менеджер по загрузке данных ip из файла
    """
    _CHOICE_UPLOADING_BY_FORMAT = {
        ".pdf": UploadIPsPDF,
        ".txt": UploadIPsText
    }

    def __init__(self, path_to_file: Path = PATH_TO_IPS_FILE):
        self.path_to_file = path_to_file
        self.object_ips = self._get_data_ips()

    def _get_data_ips(self) -> Dict[str, List[str]]:
        """
        Возвращает объект данных ip
        :return: Dict[str, List[str]]
        """
        upload_obj = self._choice_upload_by_format()
        return upload_obj.read_file()

    def _choice_upload_by_format(self) -> UploadIPsBase:
        """
        Возвращает класс работы с файлом, который соответствует тому или иному формату файла
        :return UploadIPs type
        """
        file_format = self.path_to_file.suffix
        if (upload := self._CHOICE_UPLOADING_BY_FORMAT[file_format]) is None:
            raise InvalidFormat(f"Не правильный формат файла {file_format}")
        return upload(self.path_to_file)


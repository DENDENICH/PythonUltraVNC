from typing import Dict, List
from pathlib import Path

from config import (
    PATH_TO_FAVORITE_FILE
)
from errors import InvalidFormat, FileNotFound, OtherException
from .base_date_manager import JSONBaseDataManager


class DataFavoriteManager(JSONBaseDataManager):
    """
    Класс-менеджер по работе с данными ips
    """

    def __init__(self, path_to_file: Path = PATH_TO_FAVORITE_FILE):
        super().__init__(path_to_file)

    def get_data(self) -> Dict[str, List[str]]:
        """
        Возвращает объекты данных ip
        :return: Dict[str, List[str]]
        """
        try:
            result = super().get_data()
        except FileNotFoundError:
            raise FileExistsError(f"Файл {self.path_to_file} для загрузки данных не найден")
        else:
            return result

    def upload_new(self, data: Dict[str, List[str]]) -> None:
        """
        Создать новые данные ips в файле
        
        :param data: данные типа Dict[str, List[str]]
        :return: None
        """
        try:
            super().upload_new(data)
        except FileNotFoundError:
            raise FileExistsError(f"Файл {self.path_to_file} для загрузки данных не найден")
        except Exception as e:
            raise OtherException(f"Не предвиденная ошибка - {e}")

        

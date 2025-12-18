from typing import Dict, List
from pathlib import Path

from config import (
    PATH_TO_IPS_FILE
)

from errors import InvalidFormat, OtherException, FileNotFound
from utils.validate_module import (
    validate_comment,
    validate_ip,
    validate_title
)

from .items import JsonData, IPEntry
from .base_date_manager import JSONBaseDataManager


class DataIPsManager(JSONBaseDataManager):
    """
    Класс-менеджер по работе с данными ips
    """

    def __init__(self, path_to_file: Path = PATH_TO_IPS_FILE):
        super().__init__(path_to_file)


    def get_data(self) -> JsonData:
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


    def upload_new(self, data: JsonData) -> None:
        """
        Создать новые данные ips в файле
        
        :param data: данные типа Dict[str, List[str]]
        :return: None
        """
        self._checking_data(data)
        try:
            super().upload_new(data)
        except FileNotFoundError:
            raise FileExistsError(f"Файл {self.path_to_file} для загрузки данных не найден")
        except Exception as e:
            raise OtherException(f"Не предвиденная ошибка - {e}")


    def _checking_data(self, data: JsonData) -> None:
        """
        Осуществляет проверку данных на валидные символы
        
        :param data: Добавляемые данные для проверки
        :return: None
        :exception: InvalidFormat
        """
        for title, entries in data.items():
            validate_title(title)

            # Проверка типа - ожидается список с объектами 'IPEntry'
            if not isinstance(entries, list):
                raise InvalidFormat(
                    f"Заголовок '{title}' должен содержать список IP"
                )

            for entry in entries:
                
                # Если данные ip являются не 'IPEntry'
                if not isinstance(entry, IPEntry):
                    raise ValueError(
                        f"{title}: элемент #{entry} должен быть объектом 'IPEntry'"
                    )

                # проверяем ip и комментарий
                validate_ip(entry.ip)
                validate_comment(entry.comment)

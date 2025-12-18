from typing import Dict, List
from pathlib import Path
import json

from .items import JSONDumpParams, IPEntry, JsonData


class JSONBaseDataManager:
    """
    Базовый класс по работе с данными в JSON и dict формате
    """
    def __init__(self, path_to_file: Path):
        self.path_to_file = path_to_file
        self.json_dump_params = JSONDumpParams()


    def get_data(self) -> Dict[str, List[str]]:
        """
        Возвращает объекты данных из JSON файла
        :return: Dict[str, List[str]]
        """
        with open(self.path_to_file, "r", encoding="utf-8") as f:
            pass


    def upload_new(self, data: JsonData) -> None:
        """
        Создать новые данные в JSON файле
        
        :param data: данные типа Dict[str, List[str]]
        :return: None
        """
        
        exists_data = self.get_data()
        merged = self._merge_data(exists_data, data)

        self._save(merged)


    def _merge_data(
            self, 
            exists_data: JsonData, 
            new_data: JsonData
    ) -> JsonData:
        """
        Объединяет объекты старых данных и новых
        
        :param exists_data: старые данные из файла
        :param new_data: новые данные
        :return: обновленный JSON объект
        :rtype: Dict[str, List[str]]
        """
        for title, new_entries in new_data.items():
            if (data := exists_data.get(title)) is None:
                exists_data[title] = new_entries
                continue

            for entry in new_entries:
                if not self._ip_exists(data, entry.ip):
                    exists_data[title].append(entry)

        return exists_data
        

    def _ip_exists(self, entries: List[IPEntry], new_ip: str) -> bool:
        """
        Проверка дубликатов добавляемого ip в определенный заголовок
        :param entries: данные ip существующего заголовка
        :param new_ip: новый ip
        :return: bool
        """
        return any(e.ip == new_ip for e in entries)


    def _save(self, data: JsonData) -> None:
        """
        Перезапись JSON схемы
        
        :param data: новая JSON схема
        :type data: JsonData
        """
        with open(self.path_to_file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=self.json_dump_params.ensure_ascii,
                indent=self.json_dump_params.indent
            )
            
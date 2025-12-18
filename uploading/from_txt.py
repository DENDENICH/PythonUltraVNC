from typing import Dict, List

from .base import UploadIPsBase
from errors import FileNotFound


class UploadIPsText(UploadIPsBase):
    """
    Класс для чтения текстового файла и преобразования данных в python объект
    """
    def __init__(self, path_to_file: str):
        super().__init__(path_to_file)

    def read_file(self) -> Dict[str, List[str]]:
        """
        Читает текстовый файл и формирует словарь по следующим правилам:
        - строки, обрамлённые ** в начале и в конце, становятся ключами словаря;
        - последующие строки (до следующего ключа) добавляются в список значений этого ключа.

        Returns:
            dict: сформированный словарь с ключами и списками значений
        """
        result_dict = {}
        current_key = None

        try:
            with open(self.path_to_file, 'r', encoding='utf-8') as file:
                for line in file:
                    # Удаляем символы переноса строки и пробелы по краям
                    line = line.strip()

                    # Проверяем, является ли строка ключом (обрамлена **)
                    if line.startswith('**') and line.endswith('**'):
                        # Извлекаем название ключа (убираем **)
                        key_name = line[2:-2]
                        current_key = key_name
                        # Создаём новый ключ в словаре с пустым списком значений
                        result_dict[current_key] = []

                    # Если строка не ключ и у нас есть текущий ключ, добавляем строку в список значений
                    elif current_key is not None and line:
                        if (s := "\\") in line:
                            line = line.replace(s, "/")
                        result_dict[current_key].append(line)

        except FileNotFoundError:
            raise FileNotFound()
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")

        return result_dict

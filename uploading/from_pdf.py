from pypdf import PdfReader
from typing import Dict, List

from .base import UploadIPsBase



class UploadIPsPDF(UploadIPsBase):
    """
    Класс для чтения pdf файла и преобразования данных в python объект
    """
    def __init__(self, path_to_file: str):
        super().__init__(path_to_file)

    def read_file(self) -> Dict[str, List[str]]:
        try:
            # Открываем PDF-файл
            reader = PdfReader(self.path_to_file)
            # Получаем количество страниц
            num_pages = len(reader.pages)
            print(f"Количество страниц в документе: {num_pages}\n")
            # Проходим по всем страницам и выводим текст
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                print(f"--- Страница {page_num + 1} ---")
                print(text)
        except FileNotFoundError:
            print(f"Ошибка: файл '{self.path_to_file}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при чтении PDF: {e}")
            
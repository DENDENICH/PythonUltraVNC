

class FileNotFound(Exception):
    def __init__(self, message: str = "Файл для загрузки данных не найден. Укажите путь вручную"):
        super().__init__(message)


class InvalidFormat(Exception):
    def __init__(self, message: str):
        super().__init__(message)

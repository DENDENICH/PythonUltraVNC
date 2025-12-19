
class FileNotFound(Exception):
    """
    Путь к файлам в папке data не найден
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidFormat(Exception):
    """
    Не правильный формат файла данных
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidIP(Exception):
    """
    Не валидный формат ip
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidText(Exception):
    """
    Не валидный формат названия или коментария 
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class OtherException(Exception):
    """
    Другие непредусмотренные ошибки
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message) 


import re

from errors import InvalidText, InvalidIP


_IP_PATTERN = re.compile(
    r"""
    ^
    (?P<ip>
        (25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)
        (\.
        (25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}
    )
    (?P<suffix>/[a-zA-Z0-9_-]+)?
    $
    """,
    re.VERBOSE
)
_FORBIDDEN_CHARS_PATTERN = re.compile(
    r"""
    [\n\r\t\\/]      
    """,
    re.VERBOSE
)


def validate_ip(ip: str) -> None:
    """
    Валидирует IPv4 адрес с опциональным суффиксом (/dat)
    """
    if not ip:
        raise InvalidIP("IP не может быть пустым")

    if not _IP_PATTERN.match(ip):
        raise InvalidIP(f"Некорректный IP адрес: {ip}")


def validate_title(
    value: str,
    allow_empty: bool = False,
    max_length: int = 100
) -> None:
    """
    Валидация заголовков

    :param value: проверяемое значение - комментарий или название заголовка
    :param allow_empty: разрешается быть пустым
    :param max_length: максимальная длинна строки
    :return: None
    """
    if not isinstance(value, str):
        raise InvalidText(f"Название должно быть строкой")

    _validate_text_general(value, allow_empty, max_length)


def validate_comment(
    value: str,
    allow_empty: bool = True,
    max_length: int = 100
) -> None:
    """
    Валидация комментариев к ip

    :param value: проверяемое значение - комментарий или название заголовка
    :param allow_empty: разрешается быть пустым
    :param max_length: максимальная длинна строки
    :return: None
    """
    _validate_text_general(value, allow_empty, max_length)


def _validate_text_general(
    value: str,
    allow_empty: bool,
    max_length: int
) -> None:
    value = value.strip()

    if not value and not allow_empty:
        raise InvalidText(f"Комментарий не может быть пустым")

    if len(value) > max_length:
        raise InvalidText(
            f"Комментарий превышает максимальную длину {max_length}"
        )

    if _FORBIDDEN_CHARS_PATTERN.search(value):
        raise InvalidText(
            f"Комментарий содержит запрещённые символы"
        )
    
from typing import Dict, List
from abc import ABC, abstractmethod


class UploadIPsBase(ABC):
    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    @abstractmethod
    def read_file(self) -> Dict[str, List[str]]:
        pass

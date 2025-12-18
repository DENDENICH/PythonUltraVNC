from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class JSONDumpParams:
    ensure_ascii: bool = False, 
    indent: int = 4


@dataclass
class IPEntry:
    ip: str
    comment: str = ""


JsonData = Dict[str, List[IPEntry]] 
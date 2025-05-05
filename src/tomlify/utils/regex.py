import re
from dataclasses import dataclass
from typing import Any


@dataclass
class RegexChecker:
    string: str
    match: re.Match[str] | None = None

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            other = re.compile(other)
        if not isinstance(other, re.Pattern):
            raise NotImplementedError
        self.match: re.Match[str] = other.match(self.string)
        return self.match is not None

    def __str__(self) -> str:
        if not self.match:
            return ""
        return self.match.string

    def __len__(self) -> int:
        if not self.match:
            return 0
        return self.match.endpos

    def groups(self) -> tuple[str | Any, ...]:
        if not self.match:
            return ("",)
        return self.match.groups()

    def group(self, num: int) -> str:
        if not self.match:
            return ""
        return self.match.group(num)

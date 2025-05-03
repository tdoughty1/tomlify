from __future__ import annotations

import datetime
import re
from abc import ABC
from typing import Any


def startw_with_newline(s: str) -> bool:
    return len(s) > 0 and (s[0] == "\n" or s[0] == "\r"or s[0:1] == "\r\n")

def remove_backslashed_whitespace(s: str) -> str:
    tokens = re.split(r'\\[\n\r\f]', s)
    tokens = [token if n == 0 else token.lstrip() for n, token in enumerate(tokens)]
    return "".join(tokens)

class Value(ABC):

    _raw: str

    def __str__(self) -> str:
        return self._raw


class Integer(int, Value):
    _type: str

    def __new__(cls, value: str) -> Integer:

        if value.startswith("0x"):
            obj = int.__new__(cls, value, 16)
            obj._type = "hex"
        elif value.startswith("0b"):
            obj = int.__new__(cls, value, 2)
            obj._type = "bin"
        elif value.startswith("0o"):
            obj = int.__new__(cls, value, 8)
            obj._type = "oct"
        else:
            obj = int.__new__(cls, value)
            obj._type = "int"

        obj._raw = value
        return obj

class ValueString(str, Value):
    pass

class BasicString(ValueString):
    def __new__(cls, value: str) -> BasicString:
        print(f"In __new__ with cls = {cls}, type={type(cls)}, value={value}, type(value)={type(value)}")
        raw_value = value
        value = value[1:-1]
        string = super().__new__(cls, value)
        string._raw = raw_value
        return string


class MultilineBasicString(ValueString):
    def __new__(cls, value: str) -> MultilineBasicString:
        print(f"In __new__ with cls = {cls}, type={type(cls)}, value={value}, type(value)={type(value)}")
        raw_value = value
        value = value[3:-3]
        value = value.lstrip() if startw_with_newline(value) else value
        value = remove_backslashed_whitespace(value)
        print(value)
        string = super().__new__(cls, value)
        string._raw = raw_value
        return string

class LiteralString(ValueString):
    def __new__(cls, value: str) -> LiteralString:
        print(f"In __new__ with cls = {cls}, type={type(cls)}, value={value}, type(value)={type(value)}")
        raw_value = value
        value = value[1:-1]
        string = super().__new__(cls, value)
        string._raw = raw_value
        return string

class MultilineLiteralString(ValueString):
    def __new__(cls, value: str) -> MultilineLiteralString:
        print(f"In __new__ with cls = {cls}, type={type(cls)}, value={value}")
        print(f"type(value)={type(value)}")
        raw_value = value
        value = value[3:-3]
        value = value.lstrip("\n\r") if startw_with_newline(value) else value
        print(value)
        string = super().__new__(cls, value)
        string._raw = raw_value
        return string

class Float(float, Value):
    def __new__(cls, value: str) -> Float:
        return super().__new__(cls, value)

    def __init__(self, value: str):
        if '.' in value:
            mantissa, exponent = value.split('.')
            if len(mantissa) == 0 or len(exponent) == 0:
                raise ValueError("Invalid floating point input")
            if not mantissa[-1].isdigit() or not exponent[0].isdigit():
                raise ValueError("Invalid floating point input")

        self._raw = value

    def __str__(self) -> str:
        return self._raw


class Boolean(Value):
    def __init__(self, value: str) -> None:
        if value not in ["true", "false"]:
            raise ValueError("Invalid boolean input")
        self._raw = value

    def __bool__(self) -> bool:
        return self._raw == "true"

    def __str__(self) -> str:
        return self._raw


class DateTime(datetime.datetime, Value):

    def __new__(cls, **kwargs: Any) -> DateTime:
       raw = kwargs.pop('raw')
       dt = datetime.datetime.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalDateTime(datetime.datetime, Value):

    def __new__(cls, **kwargs: Any) -> LocalDateTime:
       raw = kwargs.pop('raw')
       dt = datetime.datetime.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalDate(datetime.date, Value):

    def __new__(cls, **kwargs: Any) -> LocalDate:
       raw = kwargs.pop('raw')
       dt = datetime.date.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalTime(datetime.time, Value):

    def __new__(cls, **kwargs: Any) -> LocalTime:
       raw = kwargs.pop('raw')
       dt = super().__new__(cls, **kwargs)
       dt._raw = raw
       return dt

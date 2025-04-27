import datetime

class Value:

    def __str__(self) -> str:
        return self._raw


class Integer(int, Value):

    def __new__(cls, value):

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


class BasicString(str, Value):
    pass

class MultilineBasic(str, Value):
    pass 

class LiteralBasic(str, Value):
    pass

class MultilineLiteral(str, Value):
    pass

class Float(float, Value):
    def __new__(cls, value):
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
    def __init__(self, value):
        if value not in ["true", "false"]:
            raise ValueError("Invalid boolean input")
        self._raw = value

    def __bool__(self):
        return self._raw == "true"

    def __str__(self):
        return self._raw


class DateTime(datetime.datetime, Value):

    def __new__(cls, **kwargs):
       raw = kwargs.pop('raw')
       dt = datetime.datetime.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalDateTime(datetime.datetime, Value):

    def __new__(cls, **kwargs):
       raw = kwargs.pop('raw')
       dt = datetime.datetime.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalDate(datetime.date, Value):

    def __new__(cls, **kwargs):
       raw = kwargs.pop('raw')
       dt = datetime.date.__new__(cls, **kwargs)
       dt._raw = raw
       return dt

class LocalTime(datetime.time, Value):

    def __new__(cls, **kwargs):
       raw = kwargs.pop('raw')
       dt = super().__new__(cls, **kwargs)
       dt._raw = raw
       return dt

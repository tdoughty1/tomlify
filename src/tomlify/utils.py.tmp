import re
from datetime import timedelta, timezone

from .values import (
    BasicString,
    DateTime,
    LiteralString,
    LocalDate,
    LocalDateTime,
    LocalTime,
    MultilineBasicString,
    MultilineLiteralString,
    ValueString,
)

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

RFC_3339_DATE_STR = r'([0-9]{4,})-([0-1][0-9])-([0-3][0-9])'
RFC_3339_TIME_STR = r'([0-2][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?'
RFC_3339_SEPARATOR_STR = r'[Tt ]'
RFC_3339_TZ_STR = r'([Z])?([+-])?([0-2][0-9])?:?([0-5][0-9])?'

RFC_3339_DATETIME_STR = "".join([
    RFC_3339_DATE_STR,
    RFC_3339_SEPARATOR_STR,
    RFC_3339_TIME_STR,
    RFC_3339_TZ_STR,
])

RFC_3339_DATE_STR_PATTERN = re.compile(RFC_3339_DATE_STR)
RFC_3339_TIME_STR_PATTERN = re.compile(RFC_3339_TIME_STR)
RFC_3339_DATETIME_STR_PATTERN = re.compile(RFC_3339_DATETIME_STR)

TimeConfig = dict[str, int|str|timezone|None]
TimeObject = LocalDate|LocalTime|LocalDateTime|DateTime


def parse_date_time(date_time_str: str) -> TimeObject:

    kwargs: TimeConfig = dict()

    matches = re.match(RFC_3339_DATETIME_STR_PATTERN, date_time_str)
    if matches:

        try:
            kwargs['year'] = int(matches.group(1))
            kwargs['month'] = int(matches.group(2))
            kwargs['day'] = int(matches.group(3))
            kwargs['hour'] = int(matches.group(4))
            kwargs['minute'] = int(matches.group(5))
            kwargs['second'] = int(matches.group(6))
            kwargs['microsecond'] = int(matches.group(7)[1:]) if matches.group(7) else 0
            kwargs['raw'] = date_time_str
        except TypeError:
            raise ValueError(f"Invalid date input: {date_time_str}")

        z_char = matches.group(8)
        tz_sign = matches.group(9) if matches.group(9) else "+"
        hour_offset = int(matches.group(10)) if matches.group(10) else 0
        minute_offset = int(matches.group(11)) if matches.group(11) else 0

        if z_char or tz_sign or hour_offset or minute_offset:

            offset_seconds = hour_offset * SECONDS_PER_HOUR + minute_offset * SECONDS_PER_MINUTE
            offset = timedelta(seconds=offset_seconds)
            if tz_sign == "-":
                offset = -offset
            if hour_offset == 0 and minute_offset == 0:
                kwargs["tzinfo"] = timezone.utc
            else:
                kwargs["tzinfo"] = timezone(offset, f"{tz_sign}{hour_offset:02d}:{minute_offset:02d}")

            return DateTime(**kwargs)
        kwargs["tzinfo"] = None
        return LocalDateTime(**kwargs)


    matches = re.match(RFC_3339_DATE_STR_PATTERN, date_time_str)
    if matches:
        year, month, day = matches.groups()

        try:
            kwargs['year'] = int(year)
            kwargs['month'] = int(month)
            kwargs['day'] = int(day)
            kwargs['raw'] = date_time_str
        except TypeError:
            raise ValueError(f"Invalid date input: {date_time_str}")

        return LocalDate(**kwargs)

    matches = re.match(RFC_3339_TIME_STR_PATTERN, date_time_str)
    if matches:
        hour, minute, second, microsecond = matches.groups()

        try:
            kwargs['hour'] = int(hour)
            kwargs['minute'] = int(minute)
            kwargs['second'] = int(second)
            kwargs['microsecond'] = int(microsecond[1:]) if microsecond else 0
            kwargs['raw'] = date_time_str
        except TypeError:
            raise ValueError(f"Invalid date time input: {date_time_str}")

        return LocalTime(**kwargs)

    raise ValueError(f"Invalid date time input: {date_time_str}")



def parse_string(raw_string: str) -> ValueString:
    if raw_string.startswith('"""'):
        return MultilineBasicString(raw_string)
    if raw_string.startswith("'''"):
        return MultilineLiteralString(raw_string)
    if raw_string.startswith("'"):
        return LiteralString(raw_string)
    if raw_string.startswith('"'):
        return BasicString(raw_string)
    raise ValueError("Unknown string format")


from datetime import timedelta, timezone
import math

import pytest

from tomlify.utils import parse_date_time
from tomlify.values import Boolean, DateTime, Float, Integer, LocalDate, LocalDateTime, LocalTime



str = '''"I'm a string. \"You can quote me\". Name\tJos\u00E9\nLocation\tSF."'''


str1 = """
Roses are red
Violets are blue"""

# On a Unix system, the above multi-line string will most likely be the same as:
str2 = "Roses are red\nViolets are blue"

# On a Windows system, it will most likely be equivalent to:
str3 = "Roses are red\r\nViolets are blue"

# The following strings are byte-for-byte equivalent:
str1 = "The quick brown fox jumps over the lazy dog."

str2 = """
The quick brown \


  fox jumps over \
    the lazy dog."""

str3 = """\
       The quick brown \
       fox jumps over \
       the lazy dog.\
       """

str4 = """Here are two quotation marks: "". Simple enough."""
# str5 = """Here are three quotation marks: """."""  # INVALID
str5 = """Here are three quotation marks: ""\"."""
str6 = """Here are fifteen quotation marks: ""\"""\"""\"""\"""\"."""

# "This," she said, "is just a pointless statement."
str7 = '""""This," she said, "is just a pointless statement.""""'


# What you see is what you get.
winpath  = r'C:\Users\nodejs\templates'
winpath2 = r"'\\ServerX\admin$\system32\'"
quoted   = r'Tom "Dubs" Preston-Werner'
regex    = r"'<\i\c*\s*>'"

regex2 = r'''I [dw]on't need \d{2} apples'''
lines  = '''
The first newline is
trimmed in raw strings.
   All other whitespace
   is preserved.
'''

quot15 = '''Here are fifteen quotation marks: """""""""""""""'''

# apos15 = '''Here are fifteen apostrophes: ''''''''''''''''''  # INVALID
apos15 = "Here are fifteen apostrophes: '''''''''''''''"

# 'That,' she said, 'is still pointless.'
str = "''''That,' she said, 'is still pointless.''''"


def test_valid_integer_positive():
    input_integer_string = "+99"
    actual_output = Integer(input_integer_string)
    assert actual_output == 99
    assert actual_output._raw == input_integer_string


def test_valid_integer_no_sign():
    input_integer_string = "42"
    actual_output = Integer(input_integer_string)
    assert actual_output == 42
    assert actual_output._raw == input_integer_string 

def test_valid_integer_zero():
    input_integer_string = "0"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0
    assert actual_output._raw == input_integer_string

def test_valid_integer_negative():
    input_integer_string = "-17"
    actual_output = Integer(input_integer_string)
    assert actual_output == -17
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'int'

def test_valid_integer_one_underscore():
    input_integer_string = "1_000"
    actual_output = Integer(input_integer_string)
    assert actual_output == 1_000
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'int'

def test_valid_integer_two_underscore():
    input_integer_string = "5_349_221"
    actual_output = Integer(input_integer_string)
    assert actual_output == 5349221
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'int'

def test_valid_integer_indian_grouping():
    input_integer_string = "53_49_221"
    actual_output = Integer(input_integer_string)
    assert actual_output == 5349221
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'int'

def test_valid_integer_three_many_underscore():
    input_integer_string = "1_2_3_4_5"
    actual_output = Integer(input_integer_string)
    assert actual_output == 12345
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'int'


def test_hexidecimal_capital():
    input_integer_string = "0xDEADBEEF"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0xDEADBEEF
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'hex'

def test_hexidecimal_lower():
    input_integer_string = "0xdeadbeef"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0xdeadbeef
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'hex'

def test_hexidecimal_lower_with_underscore():
    input_integer_string = "0xdead_beef"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0xdead_beef
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'hex'

def test_octal_long():
    input_integer_string = "0o01234567"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0o01234567
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'oct'


def test_octal_long():
    input_integer_string = "0o755"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0o755
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'oct'

def test_binary():
    input_integer_string = "0b11010110"
    actual_output = Integer(input_integer_string)
    assert actual_output == 0b11010110
    assert actual_output._raw == input_integer_string
    assert actual_output._type == 'bin'

def test_valid_float_fraction_positive():
    input_float_string = "+1.0"
    actual_output = Float(input_float_string)
    assert actual_output == 1.0
    assert actual_output._raw == input_float_string

def test_valid_float_fraction_no_sign():
    input_float_string = "3.1415"
    actual_output = Float(input_float_string)
    assert actual_output == 3.1415
    assert actual_output._raw == input_float_string

def test_valid_float_fraction_negative():
    input_float_string = "-0.01"
    actual_output = Float(input_float_string)
    assert actual_output == -0.01
    assert actual_output._raw == input_float_string

def test_valid_float_post_exponent_plus():
    input_float_string = "5e+22"
    actual_output = Float(input_float_string)
    assert actual_output == 5e+22
    assert actual_output._raw == input_float_string

def test_valid_float_post_exponent_no_sign():
    input_float_string = "1e06" 
    actual_output = Float(input_float_string)
    assert actual_output == 1e06
    assert actual_output._raw == input_float_string

def test_valid_float_post_exponent_minus():
    input_float_string = "-2E-2"
    actual_output = Float(input_float_string)
    assert actual_output == -2E-2
    assert actual_output._raw == input_float_string

def test_valid_float_fractional_exponent():
    input_float_string = "6.626e-34"
    actual_output = Float(input_float_string)
    assert actual_output == 6.626e-34
    assert actual_output._raw == input_float_string


def test_invalid_float_no_leading_digit():
    input_float_string = ".7"
    with pytest.raises(ValueError):
        Float(input_float_string)


def test_invalid_float_no_trailing_digit():
    input_float_string = "7."
    with pytest.raises(ValueError):
        Float(input_float_string) 

def test_invalid_float_no_trailing_digit_before_exponent():
    input_float_string = "3.e+20"
    with pytest.raises(ValueError):
        Float(input_float_string)

def test_valid_float_underscore():
    input_float_string = "224_617.445_991_228"
    actual_output = Float(input_float_string)
    assert actual_output == 224617.445991228
    assert actual_output._raw == input_float_string

def test_valid_float_inf():
    input_float_string = "inf"
    actual_output = Float(input_float_string)
    assert math.isinf(actual_output) and actual_output > 0
    assert actual_output._raw == input_float_string

def test_valid_float_neg_inf():
    input_float_string = "-inf"
    actual_output = Float(input_float_string)
    assert math.isinf(actual_output) and actual_output < 0
    assert actual_output._raw == input_float_string

def test_valid_float_pos_inf():
    input_float_string = "+inf"
    actual_output = Float(input_float_string)
    assert math.isinf(actual_output) and actual_output > 0  
    assert actual_output._raw == input_float_string

def test_valid_float_nan():
    input_float_string = "nan"
    actual_output = Float(input_float_string)
    assert math.isnan(actual_output)
    assert actual_output._raw == input_float_string

def test_valid_float_neg_nan():
    input_float_string = "-nan"
    actual_output = Float(input_float_string)
    assert math.isnan(actual_output)
    assert actual_output._raw == input_float_string

def test_valid_float_pos_nan():
    input_float_string = "+nan"
    actual_output = Float(input_float_string)
    assert math.isnan(actual_output)
    assert actual_output._raw == input_float_string

def test_valid_boolean_true():
    input_boolean_string = "true"
    actual_output = Boolean(input_boolean_string)
    assert actual_output
    assert actual_output._raw == input_boolean_string

def test_valid_boolean_false():
    input_boolean_string = "false"
    actual_output = Boolean(input_boolean_string)
    assert not actual_output
    assert actual_output._raw == input_boolean_string

def test_invalid_boolean():
    input_boolean_string = "invalid"
    with pytest.raises(ValueError):
        Boolean(input_boolean_string)


DATE_TEST_PARAMS = {
    'year' : 1979, 
    'month': 5, 
    'day': 27, 
    'hour': 7, 
    'minute': 32, 
    'second': 0,
}


def test_valid_datetime_with_Z():
    input_kwargs = DATE_TEST_PARAMS.copy() 
    input_date_time_string = "1979-05-27T07:32:00Z"
    input_kwargs['tzinfo'] = timezone.utc
    input_kwargs['raw'] = input_date_time_string
    actual_output = parse_date_time(input_date_time_string)
    expected_output = DateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_datetime_offset():
    input_kwargs = DATE_TEST_PARAMS.copy() 
    input_date_time_string = "1979-05-27T07:32:00-07:00"
    input_kwargs['tzinfo'] = timezone(timedelta(days=-1, seconds=61200), '-07:00')
    input_kwargs['raw'] = input_date_time_string
    actual_output = parse_date_time(input_date_time_string)
    expected_output = DateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_datetime_offset_microseconds():
    input_kwargs = DATE_TEST_PARAMS.copy() 
    input_date_time_string = "1979-05-27T07:32:00.999999-07:00"
    input_kwargs['tzinfo'] = timezone(timedelta(days=-1, seconds=61200), '-07:00')
    input_kwargs['raw'] = input_date_time_string
    input_kwargs['microsecond'] = 999999
    actual_output = parse_date_time(input_date_time_string)
    expected_output = DateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_datetime_space():
    input_kwargs = DATE_TEST_PARAMS.copy() 
    input_date_time_string = "1979-05-27 07:32:00Z"
    input_kwargs['tzinfo'] = timezone.utc
    input_kwargs['raw'] = input_date_time_string
    actual_output = parse_date_time(input_date_time_string)
    expected_output = DateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_local_datetime():
    input_kwargs = DATE_TEST_PARAMS.copy()
    input_date_time_string = "1979-05-27T07:32:00" 
    input_kwargs['tzinfo'] = timezone.utc
    input_kwargs['raw'] = input_date_time_string
    actual_output = parse_date_time(input_date_time_string)
    expected_output = LocalDateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_local_datetime_microseconds():
    input_kwargs = DATE_TEST_PARAMS.copy()
    input_date_time_string = "1979-05-27T07:32:00.999999"
    input_kwargs['microsecond'] = 999999
    input_kwargs['tzinfo'] = timezone.utc
    input_kwargs['raw'] = input_date_time_string
    actual_output = parse_date_time(input_date_time_string)
    expected_output = LocalDateTime(**input_kwargs)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_local_date():
    input_date_string = "1979-05-27"
    actual_output = parse_date_time(input_date_string)
    expected_output = LocalDate(year=1979, month=5, day=27, raw=input_date_string)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_local_time():
    input_time_string = "07:32:00"
    actual_output = parse_date_time(input_time_string)
    expected_output = LocalTime(hour=7, minute=32, second=0, raw=input_time_string)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw

def test_valid_local_time_microseconds():
    input_time_string = "00:32:00.999999"
    actual_output = parse_date_time(input_time_string)
    expected_output = LocalTime(hour=0, minute=32, second=0, microsecond=999999, raw=input_time_string)
    assert actual_output == expected_output
    assert actual_output._raw == expected_output._raw
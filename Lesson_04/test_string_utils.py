import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_string, output_string",
    [
        ("привет", "Привет"),
        pytest.param("привет", "привет", marks=pytest.mark.xfail),
    ]
)
def test_capitilize(input_string, output_string):
    util = StringUtils()
    assert util.capitilize(input_string) == output_string


@pytest.mark.parametrize(
    "input_string, output_string",
    [
        ("    Привет", "Привет"),
        (" Пока", "Пока"),
    ]
)
def test_trim(input_string, output_string):
    util = StringUtils()
    assert util.trim(input_string) == output_string


@pytest.mark.parametrize(
    "input_string, delimeter, output_string",
    [
        (("a-b-c-d"), "-", ["a", "b", "c", "d"]),
        (("a b c d"), " ", ["a", "b", "c", "d"]),
        pytest.param((" "), " ", [], marks=pytest.mark.xfail),
    ]
)
def test_to_list(input_string, delimeter, output_string):
    util = StringUtils()
    assert util.to_list(input_string, delimeter) == output_string


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "т"),
    ]
)
def test_contains_positive(input_string, symbol):
    util = StringUtils()
    assert util.contains(input_string, symbol) is True


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "ч"),
    ]
)
def test_contains_negative(input_string, symbol):
    util = StringUtils()
    assert util.contains(input_string, symbol) is False


@pytest.mark.parametrize(
    "input_string, symbol, output_string",
    [
        ("Привет", "т", "Приве"),
        pytest.param("Привет", "д", "Приве", marks=pytest.mark.xfail),
    ]
)
def test_delete_symbol(input_string, symbol, output_string):
    util = StringUtils()
    assert util.delete_symbol(input_string, symbol) == output_string


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "П"),
    ]
)
def test_starts_with_positive(input_string, symbol):
    util = StringUtils()
    assert util.starts_with(input_string, symbol) is True


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "р"),
    ]
)
def test_starts_with_negative(input_string, symbol):
    util = StringUtils()
    assert util.starts_with(input_string, symbol) is False


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "т"),
    ]
)
def test_end_with_positive(input_string, symbol):
    util = StringUtils()
    assert util.end_with(input_string, symbol) is True


@pytest.mark.parametrize(
    "input_string, symbol",
    [
        ("Привет", "е"),
    ]
)
def test_end_with_negative(input_string, symbol):
    util = StringUtils()
    assert util.end_with(input_string, symbol) is False


@pytest.mark.parametrize(
    "input_string",
    [
        (""),
        ("   "),
    ]
)
def test_is_empty_pisitive(input_string):
    util = StringUtils()
    assert util.is_empty(input_string) is True


@pytest.mark.parametrize(
    "input_string",
    [
        ("Привет"),
    ]
)
def test_is_empty_negative(input_string):
    util = StringUtils()
    assert util.is_empty(input_string) is False


@pytest.mark.parametrize(
    "input_string, joiner, output_string",
    [
        (["Sky", "Pro"], "-", "Sky-Pro"),
        pytest.param(["Sky", "Pro"], "+", "Sky-Pro", marks=pytest.mark.xfail),
    ]
)
def test_list_to_string(input_string, joiner, output_string):
    util = StringUtils()
    assert util.list_to_string(input_string, joiner) == output_string

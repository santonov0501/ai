import pytest
from parsing import parse_temperature

@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("45", 45.0),
        ("45,5", 45.5),
        (" 45 °C ", 45.0),
        ("0", 0.0),        
        ("60", 60.0), # верхняя граница
        ("-90", -90.0),    # нижняя граница
        ("−7", -7.0)
    ]
)
def test_valid_temperature(raw, expected):
    assert parse_temperature(raw) == expected

@pytest.mark.parametrize("raw", ["", None, "N/A", "--", "nan", "null"])
def test_no_data_returns_none(raw):
    assert parse_temperature(raw) is None    

@pytest.mark.parametrize("raw", ["abc", "-91", "61",  "60.1"])
def test_invalid_temperature_raises_value_error(raw):
    with pytest.raises(ValueError):
        parse_temperature(raw)

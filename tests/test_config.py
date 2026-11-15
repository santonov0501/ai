import pytest
import config
from config import ConfigError

def test_reads_env(monkeypatch):
    monkeypatch.setenv("SITE_LAT", "55.4")
    monkeypatch.setenv("SITE_LON", "23.5")
    monkeypatch.setenv("HEAT_THRESHOLD", "5.0")
    
    settings = config.load_settings()
    
    assert settings.site_lat == 55.4
    assert settings.site_lon == 23.5
    assert settings.heat_threshold == 5.0

def test_missing_env(monkeypatch):
    monkeypatch.delenv("SITE_LAT", raising=False)
    monkeypatch.delenv("SITE_LON", raising=False)
    monkeypatch.delenv("HEAT_THRESHOLD", raising=False)
    
    with pytest.raises(ConfigError):
        config.load_settings()

def test_default_heat_threshold(monkeypatch):
    monkeypatch.setenv("SITE_LAT", "55.4")
    monkeypatch.setenv("SITE_LON", "23.5")
    monkeypatch.delenv("HEAT_THRESHOLD", raising=False)
    
    settings = config.load_settings()
    
    assert settings.heat_threshold == 5.0
    assert type(settings.heat_threshold) == float


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("SITE_LAT", "abc"),
        ("SITE_LON", "xyz"),
    ],
)
def test_invalid_point_format(monkeypatch, name, value):
    monkeypatch.setenv("SITE_LAT", "55.4")
    monkeypatch.setenv("SITE_LON", "23.5")
    monkeypatch.setenv(name, value)

    with pytest.raises(ConfigError) as exc_info:
        config.load_settings()

    assert isinstance(exc_info.value.__cause__, ValueError)


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("SITE_LAT", "155"),
        ("SITE_LON", "200"),
    ],
)
def test_point_out_of_range(monkeypatch, name, value):
    monkeypatch.setenv("SITE_LAT", "55.4")
    monkeypatch.setenv("SITE_LON", "23.5")
    monkeypatch.setenv(name, value)

    with pytest.raises(ConfigError) as exc_info:
        config.load_settings()

    assert exc_info.value.__cause__ is None
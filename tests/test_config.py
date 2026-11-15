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
    monkeypatch.delenv("HEAT_THRESHOLD", raising=False)
    
    settings = config.load_settings()
    
    assert settings.heat_threshold == 5.0
    assert type(settings.heat_threshold) == float

def test_invalid_points(monkeypatch):
    monkeypatch.setenv("SITE_LAT", "abc")
    monkeypatch.setenv("SITE_LAT", "155")
    monkeypatch.setenv("SITE_LON", "xyz")
    monkeypatch.setenv("SITE_LON", "200")
    
    with pytest.raises(ConfigError):
        config.load_settings()
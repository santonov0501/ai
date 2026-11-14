import os 
from dotenv import load_dotenv


class ConfigError(Exception):
    """Ошибка в настройках приложения."""

load_dotenv()

def _get_str(name, default=None) -> str:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        if default is None:
            raise ConfigError(f"Не задана переменная {name}")
        return default
    return raw



def _get_float(name, default=None) -> float:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        if default is None:
            raise ConfigError(f"Не задана переменная {name}")
        return default
    try: 
        return float(raw.replace(",","."))
    except ValueError as e:
        raise ConfigError(f"{name} должно быть числом, получено: {raw!r}") from e

def load_settings() -> dict:
    settings = {}

    try:
        settings['SITE_LAT'] = _get_float('SITE_LAT')
        settings['SITE_LON'] = _get_float('SITE_LON')
        settings['HEAT_THRESHOLD'] = _get_float('HEAT_THRESHOLD', 5)
    except ConfigError as e:
        raise ConfigError(f"Ошибка при загрузке настроек: {e}")

    return settings


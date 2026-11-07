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







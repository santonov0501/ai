from dataclasses import dataclass
import os 
from dotenv import load_dotenv
 

class ConfigError(Exception):
    """Ошибка в настройках приложения."""



@dataclass(frozen=True)
class Settings:
    site_lat: float 
    site_lon: float 
    heat_threshold: float = 5.0

    def __post_init__(self):
        if not -90 <= float(self.site_lat) <= 90:
            raise ConfigError(f"Широта должна быть в диапазоне от -90 до 90, получено: {self.site_lat}")
        if not -180 <= float(self.site_lon) <= 180:
            raise ConfigError(f"Долгота должна быть в диапазоне от -180 до 180, получено: {self.site_lon}")

        

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
        return float(default)
    try: 
        return float(raw.replace(",","."))
    except ValueError as e:
        raise ConfigError(f"{name} должно быть числом, получено: {raw!r}") from e

def load_settings() -> Settings:
    return Settings(
        site_lat=_get_float("SITE_LAT"),
        site_lon=_get_float("SITE_LON"),
        heat_threshold=_get_float("HEAT_THRESHOLD", 5),
    )


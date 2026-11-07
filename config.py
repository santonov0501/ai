import os 
from dotenv import load_dotenv


load_dotenv()

def _require(name: str) -> str:
    value = os.getenv(name)
    if name == "LOG_LEVEL" and (value is None or value == ""):
        value = "INFO"
    if name == "HEAT_THRESHOLD" and (value is None or value == ""):
        value = "5.0"
    elif  value is None or value == "":
        raise RuntimeError(f"Не задана переменная окружения {name}. Скопируй .env.example в .env и заполни.")

        
        
    return value

def site_coordinates(name: str) -> float:
    try:
        return float(_require(name))
    except ValueError as e:
        raise RuntimeError(f"Некорректное значение координат в {name}.") from e

SITE_LAT = site_coordinates("SITE_LAT")
SITE_LON = site_coordinates("SITE_LON")
HEAT_THRESHOLD = site_coordinates("HEAT_THRESHOLD")
LOG_LEVEL = _require("LOG_LEVEL")






import os 
from dotenv import load_dotenv
import main

load_dotenv()

def _require(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Не задана переменная окружения {name}. Скопируй .env.example в .env и заполни.")
    return value

def site_coordinates(name: str) -> float:
    try:
        return float(_require(name))
    except ValueError as e:
        raise RuntimeError(f"Некорректное значение координат в {name}.") from e

SITE_LAT = site_coordinates("SITE_LAT")
SITE_LON = site_coordinates("SITE_LON")
HEAT_THRESHOLD = float(os.getenv("HEAT_THRESHOLD", "5"))
LOG_LEVEL = _require("LOG_LEVEL")


print(SITE_LAT, SITE_LON, HEAT_THRESHOLD, LOG_LEVEL)

# ai

## 0.1.5
а) RuntimeError: Не задана переменная окружения SITE_LAT. Скопируй .env.example в .env и заполни.<br>
б)ValueError: could not convert string to float: 'пятьдесят пять'<br>
в) При удалении HEAT_THRESHOLD все равно вывело 5, так как в os.getenv() стояло значение default<br><br>
продолжение б: 
```
import os 
from dotenv import load_dotenv

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
```

## 0.1.6
1. Хардкодить значения секретов - нельзя, даже приватный репозиторий не гарантирует защищенности данных. Например можно перехватить их по сети. 
2. Вернет True, `bool(os.getenv("DEBUG"))` проверяет наличие переменной окружения в .env. Чтобы вывести значение `DEBUG` - нужно убрать `bool()`, а вывести просто `os.getenv("DEBUG")`.
3. Код выполнится в стороннем модуле
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
1. доступ к репо есть у многих (коллеги, CI, форки), и его могут случайно сделать публичным;
история git хранит секрет навсегда, даже если потом его удалить;
на разных окружениях разные ключи, а в коде пришлось бы хранить их все. 
2. `os.getenv("DEBUG")` вернёт строку "false". `bool()` от любой непустой строки даёт True, поэтому и `bool("false")`, и `bool("0")` равны `True`. Если убрать `bool()`, получится строка, а не флаг.
3. Код выполнится в стороннем модуле

## Вывод sys.executable
`CompletedProcess(args=['C:\\repos\\ai\\.venv\\Scripts\\python.exe', 'config.py'], returncode=0)`

## Вывод git status
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .env.example
        modified:   .gitignore
        modified:   README.md
        modified:   config.py
        modified:   main.py
        modified:   requirements.txt
```
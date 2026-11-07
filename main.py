import sys
import logging


def main() -> int:
    
    try:
        import log_setup
        log_setup.setup_logging()
        log = logging.getLogger(__name__)
    except ImportError as e:
        print(f"Ошибка при импорте модуля логирования: {e}")
        return 6
    except Exception as e:
        logging.error("Ошибка при настройке логирования: %s", e)
        return 5
    
    try:
        import config
        from config import ConfigError as ConfigError
    except ImportError as e:
        log.critical("Критическая ошибка: Не удалось импортировать модуль конфигурации 'config'. %s", e)
        return 3
    except Exception as e:
        log.exception("Ошибка при инициализации файла конфигурации (возможно, синтаксическая ошибка внутри config.py)")
        return 4
    
    
    try:
        SITE_LAT = config._get_float('SITE_LAT')
        SITE_LON = config._get_float('SITE_LON')
        HEAT_THRESHOLD = config._get_float('HEAT_THRESHOLD', 5)
        log.info("Координаты объекта: %s, %s. Тепловой порог: %s°C", SITE_LAT, SITE_LON, HEAT_THRESHOLD)
    except ConfigError as e:
        log.error("Ошибка конфигурации: %s", e)
        return 1
    except Exception:
        log.exception("Непредвиденная ошибка")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
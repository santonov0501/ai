import sys
import logging


def main() -> int:
    
    try:
        import log_setup
        log_setup.setup_logging()
        log = logging.getLogger(__name__)
    except Exception as e:
        logging.error("Ошибка при настройке логирования: %s", e)
        return 2
    
    try:
        import config
        from config import ConfigError as ConfigError
    except Exception as e:
        log.exception("Ошибка при инициализации файла конфигурации (возможно, синтаксическая ошибка внутри config.py)")
        return 2

    try:
        import parsing
    except Exception as e:
        log.exception("Ошибка при инициализации модуля парсинга (возможно, синтаксическая ошибка внутри parsing.py)")
        return 2
    
    
    try:
        settings = config.load_settings()
        SITE_LAT = settings.site_lat
        SITE_LON = settings.site_lon
        HEAT_THRESHOLD = settings.heat_threshold
        log.info("Координаты объекта: %s, %s. Тепловой порог: %s°C", SITE_LAT, SITE_LON, HEAT_THRESHOLD)
    except ConfigError as e:
        log.error("Ошибка конфигурации: %s", e)
        return 1
    except Exception:
        log.exception("Непредвиденная ошибка")
        return 2
    

    
        
        
    try:
        temperature = parsing.parse_temperature()
    except ValueError as e:
        log.error("Ошибка при парсинге температуры: %s", e)
        return 1

    if temperature is None:
        log.info("Не удалось распарсить температуру из входного значения: %s", temperature)
        return 0

    log.info("Температура объекта: %s°C", temperature)
    
    return 0
    
    

if __name__ == "__main__":
    sys.exit(main())
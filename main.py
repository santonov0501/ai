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
        SITE_LAT = settings['SITE_LAT']
        SITE_LON = settings['SITE_LON']
        HEAT_THRESHOLD = settings['HEAT_THRESHOLD']
        log.info("Координаты объекта: %s, %s. Тепловой порог: %s°C", SITE_LAT, SITE_LON, HEAT_THRESHOLD)
    except ConfigError as e:
        log.error("Ошибка конфигурации: %s", e)
        return 1
    except Exception:
        log.exception("Непредвиденная ошибка")
        return 2
    

    try:
        test_values = ["5","+5","-3,5","-3.5","","abc",None]
        for test in test_values:
            temperature = parsing.parse_temperature(test)
            if temperature is None:
                return None
            else:
                log.info("Температура объекта: %s°C", temperature)
    except Exception:
        log.exception("Ошибка при парсинге температуры")
        return 2
    return 0
    
    

if __name__ == "__main__":
    sys.exit(main())
import os 
import logging
import config


def setup_logging(level: str | None = None) -> None:
    if level is None:
        level = os.getenv("LOG_LEVEL") or "INFO"
    level = level.strip().upper()
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    if level not in levels:
        raise config.ConfigError(f"Неизвестный уровень логирования: {level!r}.")

    logging.basicConfig(
        level=levels[level],
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log", encoding="utf-8"),
        ],
    )

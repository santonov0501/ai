import logging


logger = logging.getLogger(__name__)


def parse_temperature(raw: str | None = None) -> float | None:
    if raw is None or not raw.strip():
        logger.warning("Не задана входная температура")
        return None
    try:
        return float(raw.replace("−", "-").replace(",", "."))
    except ValueError:
        logger.warning("Входная температура должна быть числом, получено: %r", raw)
        return None

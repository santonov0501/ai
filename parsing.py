
def parse_temperature(raw: str | None = None) -> float | None:
    if raw is None or not raw.strip():
        return None
    if raw.strip().lower() in {"n/a", "--", "null"}:
        return None
    
    value = raw.replace("−", "-").replace(",", ".").replace("°C", "").strip()
    try:
        temperature = float(value)
    except ValueError as exc:
        raise ValueError(f"Невозможно преобразовать {raw!r} в число") from exc

    if not -90 <= temperature <= 60:
        raise ValueError(
            f"Температура должна быть в диапазоне от -90 до 60 градусов Цельсия, получено: {raw!r}"
        )

    return temperature

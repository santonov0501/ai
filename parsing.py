
def parse_temperature(raw: str | None = None) -> float | None:
    if raw is None or not raw.strip():
        return None
    try:
        return float(raw.replace("−", "-").replace(",", "."))
    except ValueError:
        raise ValueError()

     
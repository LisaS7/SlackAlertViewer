import config


def parse_alert(text):
    lines = text.strip().splitlines()

    # check if alert is something we care about
    if not lines or not lines[0].startswith("Service"):
        return None

    data = {
        "type": "UNKNOWN",
        "host": None,
        "service": None,
        "state": None,
    }

    matches = [type for type in config.ALERT_TYPES if type in lines[0].upper()]
    data["type"] = matches[0] if matches else "UNKNOWN"

    for i, line in enumerate(lines[1:], start=1):
        if line.startswith(config.ALERT_FIELDS):
            key, value = [text.strip() for text in line.split(":", 1)]
            data[key.lower()] = value
        elif "Additional Info" in line:
            data["message"] = "\n".join(lines[i + 1 :]).strip()

    return data

import config


def parse_alert(text):
    lines = text.strip().splitlines()

    # check if alert is something we care about
    if not lines or not lines[0].startswith("Service"):
        return None

    data = {
        "Type": "UNKNOWN",
        "Host": None,
        "Service": None,
        "State": None,
    }

    matches = [type for type in config.ALERT_TYPES if type in lines[0].upper()]
    data["Type"] = matches[0] if matches else "UNKNOWN"

    for i, line in enumerate(lines[1:], start=1):
        if line.startswith(config.ALERT_FIELDS):
            key, value = [text.strip() for text in line.split(":", 1)]
            data[key.title()] = value
        elif "Additional Info" in line:
            data["Message"] = "\n".join(lines[i + 1 :]).strip()

    return data

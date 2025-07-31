from slack_client import test_connection, parse_all_alerts
from ui import display_alerts


def main():
    test_connection()
    alerts = parse_all_alerts()

    if alerts:
        display_alerts(alerts)


if __name__ == "__main__":
    main()

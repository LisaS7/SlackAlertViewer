from slack_client import test_connection, parse_all_alerts


def main():
    test_connection()
    alerts = parse_all_alerts()

    if alerts:
        print(alerts)


if __name__ == "__main__":
    main()

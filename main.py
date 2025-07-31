from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

load_dotenv()

# ------------ Configuration ------------
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL_NAME = "check-alerts"
ALERT_TYPES = ("PROBLEM", "RECOVERY")
ALERT_FIELDS = ("Host", "Service", "State")

client = WebClient(token=SLACK_TOKEN)

try:
    response = client.auth_test()
    print(response)
except SlackApiError as e:
    print(e.response["error"])


# ------------ Utilities ------------


def get_channel_id(channel_name):
    try:
        result = client.conversations_list()
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                return channel["id"]
        print(f"Channel '{channel_name}' not found")
    except SlackApiError as e:
        print(f"Error fetching channels: {e.response['error']}")


def fetch_messages(channel_id, limit=10):
    try:
        result = client.conversations_history(channel=channel_id, limit=limit)
        messages = result["messages"]
        return messages
    except SlackApiError as e:
        print(f"Error fetching messages: {e.response['error']}")
        return []


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

    matches = [type for type in ALERT_TYPES if type in lines[0].upper()]
    data["type"] = matches[0] if matches else "UNKNOWN"

    for i, line in enumerate(lines[1:], start=1):
        if line.startswith(ALERT_FIELDS):
            key, value = [text.strip() for text in line.split(":", 1)]
            data[key.lower()] = value
        elif "Additional Info" in line:
            data["message"] = "\n".join(lines[i + 1 :]).strip()

    print(data)


# ------------ Main Loop ------------


def main():
    channel_id = get_channel_id(CHANNEL_NAME)
    if not channel_id:
        print("Channel not found")
        return

    messages = fetch_messages(channel_id)
    for msg in messages:
        parse_alert(msg.get("text", ""))


if __name__ == "__main__":
    main()

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

load_dotenv()

# ------------ Configuration ------------
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL_NAME = "check-alerts"

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


# ------------ Main Loop ------------


def main():
    channel_id = get_channel_id(CHANNEL_NAME)
    if not channel_id:
        print("Channel not found")
        return

    messages = fetch_messages(channel_id)
    for msg in messages:
        print(msg["text"])


if __name__ == "__main__":
    main()

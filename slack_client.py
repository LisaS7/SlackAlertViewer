from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import config
from utilities import parse_alert

client = WebClient(token=config.SLACK_TOKEN)


def test_connection():
    try:
        response = client.auth_test()
        team = response.get("team", "Unknown Team")
        user = response.get("user", "Unknown User")
        print(f"Connected to Slack workspace: {team} (user: {user})")
    except SlackApiError as e:
        print(f"Slack auth failed: {e.response['error']}")
        exit(1)


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


def parse_all_alerts():
    channel_id = get_channel_id(config.CHANNEL_NAME)
    if not channel_id:
        print("Channel not found")
        return

    messages = fetch_messages(channel_id)
    parsed_alerts = []
    for msg in messages:
        parsed = parse_alert(msg.get("text", ""))
        if parsed:
            parsed_alerts.append(parsed)

    return parsed_alerts

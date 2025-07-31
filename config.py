from dotenv import load_dotenv
import os

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")

CHANNEL_NAME = "check-alerts"
ALERT_TYPES = ("PROBLEM", "RECOVERY")
ALERT_FIELDS = ("Host", "Service", "State")

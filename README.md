# Slack Alerts Viewer

A simple Python tool to pull and display alerts from a Slack channel in a clean, readable format. Useful when the native Slack interface is too noisy or hard to follow.

## Features

- Connects to a Slack channel using a bot token
- Polls for new messages every 5 minutes
- Displays messages in a readable table using `rich`
- Loads sensitive configuration (like your token) from a `.env` file

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/LisaS7/slack-alerts-viewer.git
cd slack-alerts-viewer
```

### 2. Create a virtual environment
```bash
python3 -m venv venv # You might need to change python3 to python if this command doesn't work
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your .env file
Create a file named .env in the root of the project with the following contents:
SLACK_TOKEN=xoxb-your-slack-bot-token

If you don't have a Slack token you can generate one at https://api.slack.com/apps

### 5. Run the script



### macOS SSL Error: `CERTIFICATE_VERIFY_FAILED`

If you encounter an error like:
```
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```

This is a common issue on macOS when using Python installed from Python.org.
To fix it, run the following command in your terminal:

```bash
/Applications/Python\ 3.12/Install\ Certificates.command
```

This installs the required root certificates so Python can verify HTTPS connections (used by Slack's API).
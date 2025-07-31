from rich.console import Console
from rich.table import Table
import config

console = Console()


def display_alerts(alerts):
    table = Table(title="Slack Alerts")

    for name, style in config.TABLE_COLUMNS.items():
        table.add_column(name, style=style)

    for alert in alerts:
        values = get_values(alert)
        print(values)
        table.add_row(*values)

    console.print(table)


def get_values(alert):
    values = []
    for name in config.TABLE_COLUMNS:
        values.append(alert.get(name, "-"))
    return values

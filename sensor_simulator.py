"""Functions for generating and evaluating simulated environmental sensor readings."""

import random


def generate_reading():
    """Return a simulated temperature and humidity reading."""
    return {
        "temperature_c": round(random.uniform(18.0, 38.0), 1),
        "humidity_pct": round(random.uniform(30.0, 90.0), 1),
    }


def get_status(temperature_c, humidity_pct, temperature_limit=30.0, humidity_limit=75.0):
    """Return ALERT when either reading exceeds its configured limit."""
    if temperature_c > temperature_limit or humidity_pct > humidity_limit:
        return "ALERT"
    return "NORMAL"


def reading_to_csv_row(reading):
    """Convert a reading dictionary into a simple CSV row string."""
    return (
        f'{reading["timestamp"]},{reading["temperature_c"]},'
        f'{reading["humidity_pct"]},{reading["status"]}'
    )


import unittest

from sensor_simulator import generate_reading, get_status, reading_to_csv_row


class SensorSimulatorTests(unittest.TestCase):
    def test_generated_values_are_in_expected_ranges(self):
        reading = generate_reading()
        self.assertGreaterEqual(reading["temperature_c"], 18.0)
        self.assertLessEqual(reading["temperature_c"], 38.0)
        self.assertGreaterEqual(reading["humidity_pct"], 30.0)
        self.assertLessEqual(reading["humidity_pct"], 90.0)

    def test_normal_status(self):
        self.assertEqual(get_status(25.0, 50.0), "NORMAL")

    def test_temperature_alert(self):
        self.assertEqual(get_status(35.0, 50.0), "ALERT")

    def test_humidity_alert(self):
        self.assertEqual(get_status(25.0, 80.0), "ALERT")

    def test_limit_boundary(self):
        self.assertEqual(get_status(30.0, 75.0), "NORMAL")

    def test_csv_row_format(self):
        reading = {
            "timestamp": "2026-10-28 12:00:00",
            "temperature_c": 24.5,
            "humidity_pct": 48.0,
            "status": "NORMAL",
        }
        self.assertEqual(
            reading_to_csv_row(reading),
            "2026-10-28 12:00:00,24.5,48.0,NORMAL",
        )


if __name__ == "__main__":
    unittest.main()

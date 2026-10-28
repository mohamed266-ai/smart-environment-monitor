# Smart Environmental Monitoring System (IoT)

A beginner-friendly environmental monitoring dashboard built with Python and Streamlit. The first version simulates temperature and humidity readings so the project can be developed and tested without physical hardware.

## Features

- Simulated temperature and humidity readings
- Configurable temperature and humidity alert thresholds
- Status indicator (`NORMAL` or `ALERT`)
- Reading history and line chart
- CSV download for collected readings
- Unit tests for the sensor simulation and alert logic
- Planned upgrade path to ESP32 + DHT22 sensor hardware

> **Important:** Simulation mode does not measure real environmental conditions. Clearly label it as a simulation in demos and resumes until hardware is connected.

## Demo preview

When running, the app displays temperature, humidity, status, history, a chart, and a CSV download button.

## Requirements

- Python 3.10 or newer
- Git (for publishing to GitHub)
- Optional: Visual Studio Code

## Run locally (Windows)

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. Open a terminal in this project folder.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

6. Open the local URL printed in the terminal (usually `http://localhost:8501`).

## Run locally (macOS / Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

The tests check generated reading ranges, normal and alert states, threshold boundary behavior, and CSV row formatting.

## Project structure

```text
smart-environment-monitor/
├── app.py
├── sensor_simulator.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_sensor_simulator.py
```

## How it works

1. `sensor_simulator.py` generates plausible simulated temperature and humidity values.
2. `get_status()` compares readings against the selected alert limits.
3. `app.py` displays the readings and history in a Streamlit dashboard.
4. The CSV download lets users save the displayed history.

## Roadmap

- [x] Simulated sensor readings
- [x] Dashboard and configurable alerts
- [x] CSV export
- [x] Unit tests
- [ ] Read real sensor values from an ESP32
- [ ] Add DHT22/AM2302 temperature-humidity sensor
- [ ] Send readings over Wi-Fi using HTTP or MQTT
- [ ] Add persistent storage and deployment

## Hardware upgrade (future work)

Suggested hardware:
- ESP32 development board
- DHT22 / AM2302 temperature-humidity sensor
- Breadboard and jumper wires

For the hardware version, replace the simulated `generate_reading()` function with a safe, validated data input from the ESP32. Check the sensor and board voltage requirements before wiring.

## Publish to GitHub

Create a **public** repository named `smart-environment-monitor` on GitHub. Do not initialize it with a README if you already have this local project README. Then, in this project folder, run:

```bash
git init
git add .
git commit -m "Build smart environmental monitoring dashboard"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/smart-environment-monitor.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub may ask you to authenticate through a browser or credential manager. Never put passwords or access tokens in your source code.

## Deploy the dashboard (optional)

After pushing to GitHub:
1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Choose **Create app** and select your repository.
3. Set the main file path to `app.py`.
4. Deploy and test the public app URL.

## Resume description

**Smart Environmental Monitoring System | Python, Streamlit, IoT Simulation**

- Developed a Python dashboard to simulate temperature and humidity monitoring with configurable threshold alerts.
- Implemented reading history, visual trend charts, CSV export, and unit tests.
- Designed a modular codebase with a roadmap for ESP32-based real sensor integration.

Only claim hardware integration after you have built and tested the hardware version.

## License

This project is shared for educational and portfolio use. Add an open-source license if you want to specify reuse permissions.

# Virtual Security Operations Center (VSOC)

A Python-based educational VSOC demonstration with a Flask dashboard. It illustrates a basic workflow for collecting sample logs, flagging log lines containing the word `threat`, displaying alerts, and simulating incident-response actions.

## Features

- Flask web dashboard with **Logs**, **Threats Detected**, and **Alerts** panels
- Sample asynchronous log collection
- Basic keyword-based threat detection
- Console alerts and simulated incident response
- Rotating application log file (`vsoc.log`)
- JSON endpoint at `/api/status`

## Project structure

```text
Virtual-SOC/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── VSOC_Project_Report.pdf
└── src/
    ├── alerting.py
    ├── dashboard.py
    ├── incident_response.py
    ├── log_management.py
    ├── main.py
    └── threat_intelligence.py
```

## Requirements

- Python 3.8 or later
- pip
- Flask (installed from `requirements.txt`)

## Installation and run

Run these commands from the repository root.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/dashboard.py
```

If PowerShell blocks activation, you can run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/dashboard.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/dashboard.py
```

Open `http://127.0.0.1:5000` in your browser. Stop the server with `Ctrl+C`.

## How it works

1. `dashboard.py` starts the Flask web server and a background monitoring thread.
2. `log_management.py` generates sample log events and flags lines containing `threat`.
3. `threat_intelligence.py` adds a placeholder demo label.
4. `alerting.py` prints alert messages.
5. `incident_response.py` prints simulated response messages.
6. The browser polls `/api/status` every three seconds to refresh the dashboard.

## Important limitations

This repository is an **educational prototype**, not a production SOC or a real SIEM/IDS/SOAR deployment. It uses sample logs and simple keyword matching. It does not connect to real endpoints, external threat-intelligence feeds, cloud services, email/SMS alerting, or perform real containment actions. Do not use its output as the sole basis for security decisions.

## Project report

The submitted mini-project report is available in [`docs/VSOC_Project_Report.pdf`](docs/VSOC_Project_Report.pdf).

## Responsible use

Use this project for learning, demonstrations, and authorized defensive testing only.

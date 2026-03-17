<h1 align="center">Suspicious Login Detector</h1>
<p align="center">
  <img width="400" height="335" alt="Dashboard" src="https://github.com/user-attachments/assets/d7754f4e-dad1-4e8e-8229-c54e93717ed9" />
</p>

<p align="center">
  <img width="828" height="153" alt="Alerts" src="https://github.com/user-attachments/assets/8eda8674-c8f5-4595-a2aa-f2069f057897" />
</p>



A Python-based security monitoring tool that analyzes authentication logs and detects suspicious login activity using rule-based threat detection. The project simulates a lightweight Security Operations Center (SOC) workflow by identifying potentially malicious behavior and surfacing structured alerts for review.

## Overview
This project aims to create a lightweight login threat detection system that processes authentication events and flags suspicious patterns such as brute-force attempts, unusual login times, impossible travel, and access from blacklisted IPs.

The system is designed as a cybersecurity project that demonstrates log analysis, rule based detection, and alerts in a practical format.

## Features
- Brute-force login detection
- Blacklisted IP detection
- Off-hours login anomaly detection
- Impossible travel detection
- Alert severity classification
- Structured JSON-based log parsing
- Designed for future dashboard integration

## Tech Stack
- Python
- JSON
- FastAPI / Flask (planned)
- React or Streamlit (planned dashboard)
- GitHub
- Nmap (optional future enrichment)

## Project Structure


```
suspicious-login-detector/
│
├── backend/
│   ├── detector.py
│   ├── sample_logs.json
│   ├── blacklist.json
│   └── app.py
│
├── frontend/
│   └── dashboard/ (planned)
│
└── README.md
```

## Future Improvements
- Real-time alert dashboard
- Location based login visualization
- IP reputation / threat intelligence API integration
- Simulated IP block and unblock actions

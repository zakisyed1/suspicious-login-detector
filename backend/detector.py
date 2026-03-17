import json
from datetime import datetime

print("RUNNING SCRIPT...\n")

with open("sample_logs.json", "r") as f:
    logs = json.load(f)

with open("blacklist.json", "r") as f:
    blacklist = json.load(f)

print("=== Alerts ===\n")

for log in logs:
    print("Checking log:", log)

    if log["ip"] in blacklist:
        print(f"[HIGH] Blacklisted IP detected: {log['ip']} (User: {log['username']})")

    if log["status"] == "failed":
        print(f"[WARNING] Failed login from {log['ip']}")

    timestamp = datetime.fromisoformat(log["timestamp"])
    hour = timestamp.hour

    if log["status"] == "success" and (hour < 6 or hour >= 22):
        print(f"[MEDIUM] Off-hours login detected for {log['username']} at {timestamp.strftime('%H:%M')}")
# PyNetWatch-Lite 🛡️
**An Automated Network Device Health Monitor for Enterprise Infrastructure.**

PyNetWatch-Lite is a Python-based tool designed to automate the monitoring of network devices (Routers/Switches) via SSH. It collects real-time metrics such as CPU usage, memory utilization, and uptime, logging them into a CSV report for auditing and performance analysis.

### 🚀 Key Features
* **Multi-Vendor Support:** Compatible with Cisco IOS, Juniper, Arista, and HP through the Netmiko library.
* **Error Resilience:** Includes robust error handling for Authentication and Connection timeouts.
* **Data Logging:** Automatically generates a time-stamped `reports.csv` for historical tracking.
* **Scalable:** Easily add or remove devices from the monitoring list.

### 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** Netmiko, CSV, Datetime
* **Protocol:** SSH

### 📋 Prerequisites
Ensure you have Python installed and the Netmiko library:
```bash
pip install netmiko
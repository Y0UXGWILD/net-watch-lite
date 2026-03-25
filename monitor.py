import csv
import os
from datetime import datetime
from netmiko import ConnectHandler

# Configuration: We will use a dummy IP first to PROVE the CSV works
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '1.1.1.1',  # Fake IP to trigger the 'Offline' logic
        'username': 'admin',
        'password': 'password123',
    }
]

def get_stats(device):
    print(f"[*] Step 1: Attempting to contact {device['host']}...")
    try:
        # This will fail because 1.1.1.1 is not a router
        with ConnectHandler(**device) as net_connect:
            return {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "IP": device['host'],
                "CPU_Usage": "5%", 
                "Memory_Status": "80MB Free",
                "Status": "ONLINE"
            }
    except Exception as e:
        print(f"[!] Step 2: Connection failed as expected. Error: {type(e).__name__}")
        # Even if it fails, we return this data to be saved!
        return {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "IP": device['host'],
            "CPU_Usage": "N/A",
            "Memory_Status": "N/A",
            "Status": "OFFLINE"
        }

def save_report(data):
    print(f"[*] Step 3: Opening data/reports.csv to write data...")
    if not os.path.exists('data'):
        os.makedirs('data')
        print("[*] Created 'data' folder.")
    
    file_path = 'data/reports.csv'
    file_exists = os.path.isfile(file_path)

    # 'a' means Append (Add to the end), 'w' would overwrite it
    with open(file_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Timestamp", "IP", "CPU_Usage", "Memory_Status", "Status"])
        if not file_exists:
            writer.writeheader()
            print("[*] Wrote Header to CSV.")
        writer.writerow(data)
        print("[*] Step 4: Data successfully written to CSV!")

if __name__ == "__main__":
    print("--- PyNetWatch-Lite Debug Mode ---")
    for dev in devices:
        result = get_stats(dev)
        save_report(result)
    print("--- Script Finished ---")
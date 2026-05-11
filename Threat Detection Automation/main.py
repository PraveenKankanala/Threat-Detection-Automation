import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# Ensure the output directory exists
if not os.path.exists("output"):
    os.makedirs("output")

# 1. Read logs
log_file_path = "logs/ssh_logs.txt"
failed_ips = []

try:
    with open(log_file_path, "r", encoding="utf-8", errors="ignore") as file:
        logs = file.readlines()
except FileNotFoundError:
    print(f"Error: The file {log_file_path} was not found.")
    logs = []

# 2. Detect failed login IPs
for line in logs:
    if "Failed password" in line:
        # Regex to find IP addresses
        ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        if ip_match:
            failed_ips.append(ip_match.group(1))

# 3. Count attacks
counter = Counter(failed_ips)

# 4. Print suspicious IPs and Threat Report
print("\n=== Threat Report ===")
for ip, count in counter.items():
    level = "LOW"
    if count >= 10:
        level = "HIGH"
    elif count >= 5:
        level = "MEDIUM"
    
    print(f"{ip} -> {count} attempts [{level}]")

# 5. Create the data table
df = pd.DataFrame(counter.items(), columns=["IP Address", "Attempts"])
df["Attempts"] = pd.to_numeric(df["Attempts"])

# Save to CSV
df.to_csv("output/threat_report.csv", index=False)

# 6. Generate Graphs
if not df.empty:
    # Create a figure with two subplots (1 row, 2 columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # --- Bar Graph ---
    df.plot(kind="bar", x="IP Address", y="Attempts", ax=ax1, color='skyblue', legend=False)
    ax1.set_title("SSH Threat Detection (Bar Chart)")
    ax1.set_ylabel("Failed Attempts")
    ax1.set_xticklabels(df["IP Address"], rotation=45, ha='right')

    # --- Pie Graph ---
    ax2.pie(df["Attempts"], labels=df["IP Address"], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    ax2.set_title("Threat Distribution by IP (Pie Chart)")

    plt.tight_layout()
    
    # Save and Show
    plt.savefig("output/threat_graphs.png")
    print("\nGraphs have been saved to 'output/threat_graphs.png'")
    plt.show()
else:
    print("\nNo failed login attempts detected. Graphs will not be generated.")
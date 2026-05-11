# Threat Detection Automation Using Python

## Overview
This project is an automated cybersecurity threat detection system developed using Python. The system analyzes SSH authentication logs to identify suspicious activities such as repeated failed login attempts and potential brute-force attacks.

The project detects malicious IP addresses, classifies threat levels, generates CSV reports, and visualizes attack patterns using graphs.

## Features
- SSH log analysis
- Failed login detection
- Suspicious IP identification
- Threat level classification (LOW, MEDIUM, HIGH)
- Automated CSV report generation
- Graph visualization of attacks
- Cybersecurity monitoring automation

## Technologies Used
- Python
- Pandas
- Matplotlib
- Regular Expressions (Regex)
- VS Code

## Project Structure

Threat-Detection-Automation/
│
├── logs/
├── output/
├── main.py
├── requirements.txt
└── README.md

## How It Works
1. Reads SSH authentication logs
2. Detects failed password attempts
3. Extracts suspicious IP addresses
4. Counts attack attempts
5. Classifies threat severity
6. Generates reports and graphs automatically


## Sample Output

192.168.1.10 -> 12 attempts [HIGH]
10.0.0.5 -> 5 attempts [MEDIUM]


## Future Improvements
- Real-time monitoring
- Email alerts
- Machine learning anomaly detection
- SIEM dashboard integration
- Live network traffic analysis


## Author
Praveen Reddy Kankanala
Cybersecurity & Python Enthusiast

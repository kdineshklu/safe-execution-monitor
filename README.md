# 🛡️ Safe Execution Behavior Monitor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Linux](https://img.shields.io/badge/Platform-Linux-green)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Bash](https://img.shields.io/badge/Bash-Scripting-black)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner--Friendly-brightgreen)
![Ethical Use](https://img.shields.io/badge/Usage-Ethical%20Only-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A safe, educational, and ethical behavior analysis toolkit designed to observe system-level and network-level behavior of programs in a controlled environment.
Ideal for cybersecurity students, SOC beginners, and malware analysis fundamentals.

📑 Table of Contents

Overview

Key Features

Ethical Use Disclaimer

Requirements

Installation

Project Structure

Usage (CLI Mode)

Usage (Python GUI)

Output & Reports

Safe Execution Practices

Common Errors & Fixes

Educational Use

Future Enhancements

License

🔍 Overview

The Safe Execution Behavior Monitor provides a controlled and repeatable way to execute programs while capturing:

System calls and file access using strace

Network activity using tcpdump

Automated behavior summaries

Beginner-friendly Python UI

This project mimics real-world malware behavior analysis workflows while maintaining safety and ethical constraints.

✨ Key Features
Core Capabilities

Safe execution using time limits

System call tracing (strace)

Network traffic capture (tcpdump)

Automated behavior report generation

Python GUI for non-technical users

Fully documented, beginner-friendly setup

Safety Features

No aggressive scanning

No kernel modification

No persistence mechanisms

Time-bound execution

Designed for trusted sample programs only

⚠️ Ethical Use Disclaimer
✅ Authorized Use Only

This tool is intended ONLY for:

Educational cybersecurity labs

Personal learning environments

Authorized internal analysis

Controlled testing of trusted programs

❌ Prohibited Use

Running real malware on host systems

Analyzing programs without permission

Monitoring external networks

Any illegal or unethical activity

Unauthorized behavior analysis may be illegal.
By using this project, you agree to use it ethically and responsibly.

🧰 Requirements
System Requirements

OS: Linux (Ubuntu / Kali / Debian)

Python: 3.8 or higher

Root access (required for tcpdump)

Basic terminal knowledge

System Dependencies

Install using apt:

sudo apt update
sudo apt install -y strace tcpdump curl python3 python3-tk

Python Dependencies
pip3 install -r requirements.txt

⚙️ Installation
Step 1: Clone the Repository
git clone https://github.com/kdineshklu/safe-execution-monitor.git
cd safe-execution-monitor

Step 2: Give Execution Permissions
chmod +x scripts/*.sh
chmod +x samples/*.sh

Step 3: Verify Setup (Optional)
ls scripts
ls samples

📁 Project Structure
safe-execution-monitor/
│
├── samples/              # Test programs
├── scripts/              # Bash orchestration
├── logs/                 # Raw behavior logs
├── reports/              # Final analysis reports
├── ui/                   # Python GUI
├── requirements.txt
├── BEFORE_RUNNING.txt
├── HOW_TO_USE.txt
└── README.md

▶️ Usage — Command Line Mode
1️⃣ Capture Network Activity (sudo required)
sudo scripts/monitor_tcpdump.sh samples/test_program.sh

2️⃣ Capture System Calls
scripts/monitor_strace.sh samples/test_program.sh

3️⃣ Generate Behavior Report
scripts/generate_report.sh

4️⃣ View Report
cat reports/behavior_report.txt

🖥️ Usage — Python GUI Mode

Recommended for beginners

Run the UI:

sudo python3 ui/app.py

GUI Workflow

Click Select Program

Choose a sample script

Click Run Analysis

View report inside the UI

📄 Output & Reports
Logs

logs/strace.log → system behavior

logs/tcpdump.pcap → network activity

Final Report

reports/behavior_report.txt

Report includes:

System call counts

File access indicators

Network connection preview

🔐 Safe Execution Practices

Uses time-limited execution

Avoids root execution for target programs

No persistence or modification of system files

Designed for sandbox-like behavior observation

🛠️ Common Errors & Fixes
Permission Denied
chmod +x scripts/*.sh

Tkinter Not Found
sudo apt install python3-tk

tcpdump Permission Error
Run using sudo

🎓 Educational Use

This project is suitable for:

Cybersecurity coursework

SOC analyst fundamentals

Malware analysis basics

Linux security learning

Internship portfolios

🚀 Future Enhancements

Risk scoring engine

Suspicious behavior detection

PDF report export

Dark mode UI

Docker-based sandbox

Hash reputation checks

📜 License

This project is released for educational purposes only.
Use responsibly and ethically.

⭐ Final Note

If you can explain this project clearly, you already understand:

How analysts observe behavior

How malware analysis begins

How system & network telemetry works

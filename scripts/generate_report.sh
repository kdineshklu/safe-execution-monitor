#!/bin/bash

echo "Behavior Summary Report" > reports/behavior_report.txt
echo "======================" >> reports/behavior_report.txt

echo "" >> reports/behavior_report.txt
echo "System Call Activity:" >> reports/behavior_report.txt
grep "open(" logs/strace.log | wc -l >> reports/behavior_report.txt

echo "" >> reports/behavior_report.txt
echo "Network Activity (Preview):" >> reports/behavior_report.txt
tcpdump -r logs/tcpdump.pcap 2>/dev/null | head -n 5 >> reports/behavior_report.txt

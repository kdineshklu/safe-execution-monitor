#!/bin/bash

PROGRAM=$1
INTERFACE=any

echo "[+] Starting tcpdump..."
tcpdump -i $INTERFACE -w logs/tcpdump.pcap &
TCPDUMP_PID=$!

sleep 1
bash "$PROGRAM"
sleep 1

kill $TCPDUMP_PID
echo "[+] Network capture saved"

#!/bin/bash

PROGRAM=$1

mkdir -p logs reports

echo "[+] Running program safely..."
timeout 20s bash "$PROGRAM"
echo "[+] Execution completed"

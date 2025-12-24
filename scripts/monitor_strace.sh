#!/bin/bash

PROGRAM=$1

echo "[+] Capturing system calls..."
strace -f -o logs/strace.log bash "$PROGRAM"
echo "[+] strace log saved"

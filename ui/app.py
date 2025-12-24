import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
REPORT_PATH = os.path.join(BASE_DIR, "reports", "behavior_report.txt")

selected_file = ""

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename(
        title="Select program to analyze",
        initialdir=os.path.join(BASE_DIR, "samples")
    )
    file_label.config(text=selected_file)

def run_analysis():
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first")
        return

    try:
        messagebox.showinfo("Info", "Analysis started.\nThis may take a few seconds.")

        subprocess.run(
            ["sudo", os.path.join(SCRIPTS_DIR, "monitor_tcpdump.sh"), selected_file],
            check=True
        )
        subprocess.run(
            [os.path.join(SCRIPTS_DIR, "monitor_strace.sh"), selected_file],
            check=True
        )
        subprocess.run(
            [os.path.join(SCRIPTS_DIR, "generate_report.sh")],
            check=True
        )

        show_report()

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Analysis failed. Run app with sudo.")

def show_report():
    report_box.delete(1.0, tk.END)

    if os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "r") as f:
            report_box.insert(tk.END, f.read())
    else:
        report_box.insert(tk.END, "Report not found.")

# UI Window
root = tk.Tk()
root.title("Safe Execution Behavior Monitor")
root.geometry("700x500")

title = tk.Label(root, text="Safe Execution Behavior Monitor", font=("Arial", 16, "bold"))
title.pack(pady=10)

select_btn = tk.Button(root, text="Select Program", command=select_file)
select_btn.pack()

file_label = tk.Label(root, text="No file selected", fg="blue")
file_label.pack(pady=5)

run_btn = tk.Button(root, text="Run Analysis", bg="red", fg="white", command=run_analysis)
run_btn.pack(pady=10)

report_box = scrolledtext.ScrolledText(root, width=80, height=20)
report_box.pack(pady=10)

root.mainloop()

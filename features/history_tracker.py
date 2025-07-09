import tkinter as tk
import csv
import os
from tkinter import messagebox

history_file = "data/weather_history.csv"

def save_weather(city, temp, desc):
    os.makedirs(os.path.dirname(history_file), exist_ok=True)

    # Create file with headers if it doesn't exist
    if not os.path.exists(history_file):
        with open(history_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["City", "Temperature (°F)", "Description"])

    with open(history_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([city, temp, desc])

def show_history_window(root):
    history_window = tk.Toplevel(root)
    history_window.title("📜 Weather History")
    history_window.geometry("420x380")
    history_window.config(bg="#dfe6e9")

    title_label = tk.Label(history_window, text="Weather History", font=("Arial", 16, "bold"), bg="#dfe6e9")
    title_label.pack(pady=10)

    history_text = tk.Text(history_window, width=50, height=12, font=("Arial", 12))
    history_text.pack(pady=10)

    # Load history if it exists
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            lines = f.readlines()
            if lines:
                for line in lines:
                    history_text.insert(tk.END, line)
            else:
                history_text.insert(tk.END, "No weather history found.")
    else:
        history_text.insert(tk.END, "No weather history found.")

    history_text.config(state=tk.DISABLED)

    # --- Buttons Frame ---
    btn_frame = tk.Frame(history_window, bg="#dfe6e9")
    btn_frame.pack(pady=10)

    def clear_history():
        if os.path.exists(history_file):
            os.remove(history_file)
            messagebox.showinfo("History Cleared", "Weather history has been cleared.")
            history_window.destroy()

    clear_btn = tk.Button(btn_frame, text="Clear History", font=("Arial", 12), bg="#ffeaa7", command=clear_history)
    clear_btn.pack(side=tk.LEFT, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", font=("Arial", 12), bg="#fab1a0", command=history_window.destroy)
    close_btn.pack(side=tk.LEFT, padx=10)

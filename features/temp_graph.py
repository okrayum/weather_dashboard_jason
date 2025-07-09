import csv
import os
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_graph_window(parent):
    graph_window = tk.Toplevel(parent)
    graph_window.title("📈 Temperature Graph")
    graph_window.geometry("550x450")
    graph_window.config(bg="#dfe6e9")

    title_label = tk.Label(graph_window, text="Recent Temperature Trends", font=("Arial", 16, "bold"), bg="#dfe6e9")
    title_label.pack(pady=10)

    history_file = "data/weather_history.csv"

    if not os.path.exists(history_file):
        tk.Label(graph_window, text="No weather history available.", font=("Arial", 12), bg="#dfe6e9").pack(pady=20)
        return

    temps = []
    cities = []

    with open(history_file, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row

        for row in reader:
            if len(row) >= 2:
                cities.append(row[0])
                temps.append(float(row[1]))

    if not temps:
        tk.Label(graph_window, text="No temperature data found.", font=("Arial", 12), bg="#dfe6e9").pack(pady=20)
        return

    fig = Figure(figsize=(5.5, 3.8), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(cities, temps, marker="o", color="#0984e3")
    ax.set_title("Temperature by City", fontsize=12)
    ax.set_ylabel("Temperature (°F)")
    ax.set_xlabel("City")
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    close_btn = tk.Button(graph_window, text="Close", font=("Arial", 12), bg="#fab1a0", command=graph_window.destroy)
    close_btn.pack(pady=10)

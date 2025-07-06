import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_temperature_graph(master_window):
    # Load your CSV data
    df = pd.read_csv("data/weather_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    # Create the figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df["Date"], df["Temperature"], marker='o')

    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°F)")
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    # Create new Tkinter window for the graph
    graph_window = Toplevel(master_window)
    graph_window.title("Temperature Graph")

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

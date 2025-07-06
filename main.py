import tkinter as tk
from tkinter import messagebox
import requests
import config
import csv
from datetime import datetime

from features.temp_graph import show_temperature_graph

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        # Clear previous text
        output_text.delete(1.0, tk.END)

        # Extract and display data
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        output = f"City: {city}\nTemperature: {temp}°F\nDescription: {desc}"
        output_text.insert(tk.END, output)

        # Save to CSV
        save_weather_to_csv(city, temp, desc)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_weather_to_csv(city, temp, desc):
    filename = "data/weather_data.csv"
    fieldnames = ["Date", "City", "Temperature (°F)", "Description"]

    # Create file and write header if it doesn't exist
    try:
        with open(filename, mode="x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass  # File already exists

    # Append new weather data
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "City": city,
            "Temperature (°F)": temp,
            "Description": desc
        })        

# Main window setup
root = tk.Tk()
root.title("Weather Dashboard")

# City entry
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

# GUI setup
# Graph button
graph_button = tk.Button(root, text="Show Temperature Graph", command=lambda: show_temperature_graph(root))
graph_button.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack(pady=5)

# Text output
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

# Run the app
root.mainloop()

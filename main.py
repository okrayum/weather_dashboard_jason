import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import os
from config import API_KEY
from features import history_tracker, temp_graph, favorite_cities

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        weather_label.config(text=f"{city}: {temp}°F, {desc}")
        history_tracker.save_weather(city, temp, desc)
        update_mascot(desc)
        status_bar.config(text="Weather updated successfully.", bg="#dfe6e9")

        city_entry.delete(0, tk.END)

    except requests.exceptions.RequestException:
        messagebox.showerror("Connection Error", "Failed to fetch data.")
        status_bar.config(text="Failed to fetch data.", bg="#fab1a0")

def show_history():
    history_tracker.show_history_window(root)

def show_graph():
    temp_graph.show_graph_window(root)

def manage_favorites():
    favorite_cities.show_favorites_window(root)

def update_mascot(description: str):
    try:
        desc_lower = description.lower()
        if 'sun' in desc_lower:
            img_name = "sunny.png"
        elif 'cloud' in desc_lower:
            img_name = "cloudy.png"
        elif 'rain' in desc_lower:
            img_name = "rainy.png"
        elif 'storm' in desc_lower:
            img_name = "stormy.png"
        elif 'snow' in desc_lower:
            img_name = "snowy.png"
        elif 'fog' in desc_lower or 'mist' in desc_lower:
            img_name = "foggy.png"
        else:
            img_name = "sunny.png"

        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_dir, "assets", img_name)
        mascot_img = ImageTk.PhotoImage(Image.open(img_path).resize((140, 140)))
        mascot_label.config(image=mascot_img)
        mascot_label.image = mascot_img  # type: ignore[attr-defined]

    except FileNotFoundError:
        mascot_label.config(text="(Mascot image missing)", image='')

# --- Main Window ---
root = tk.Tk()
root.title("Jason's Weather Dashboard")
root.geometry("600x600")
root.config(bg="#dfe6e9")

# --- Title ---
title_label = tk.Label(root, text="🌤️ Jason's Weather Dashboard", font=("Arial", 20, "bold"), bg="#dfe6e9")
title_label.pack(pady=15)

# --- City Entry ---
city_frame = tk.Frame(root, bg="#dfe6e9")
city_frame.pack(pady=10)

city_label = tk.Label(city_frame, text="Enter City:", font=("Arial", 14), bg="#dfe6e9")
city_label.pack(side=tk.LEFT, padx=5)

city_entry = tk.Entry(city_frame, font=("Arial", 14), width=20)
city_entry.pack(side=tk.LEFT, padx=5)

get_weather_btn = tk.Button(city_frame, text="Get Weather", font=("Arial", 12), bg="#74b9ff", command=get_weather)
get_weather_btn.pack(side=tk.LEFT, padx=5)

# Bind Enter key to trigger Get Weather
city_entry.bind("<Return>", lambda event: get_weather())

# --- Weather Display ---
weather_label = tk.Label(root, text="Weather info will appear here.", font=("Arial", 16), bg="#dfe6e9")
weather_label.pack(pady=20)

# --- Mascot Image ---
mascot_label = tk.Label(root, bg="#dfe6e9")
mascot_label.pack(pady=10)

# --- Feature Buttons ---
btn_frame = tk.Frame(root, bg="#dfe6e9")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="📜 View History", font=("Arial", 12), bg="#fab1a0", command=show_history, width=18).pack(pady=5)
tk.Button(btn_frame, text="📈 Temperature Graph", font=("Arial", 12), bg="#ffeaa7", command=show_graph, width=18).pack(pady=5)
tk.Button(btn_frame, text="⭐ Favorites", font=("Arial", 12), bg="#55efc4", command=manage_favorites, width=18).pack(pady=5)
tk.Button(btn_frame, text="❌ Exit", font=("Arial", 12), bg="#ffeaa7", command=root.destroy, width=18).pack(pady=5)

# --- Status Bar ---
status_bar = tk.Label(root, text="Welcome to the dashboard!", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10), bg="#dfe6e9")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()

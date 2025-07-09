import tkinter as tk
import os

favorites_file = "data/favorites.txt"

def add_favorite(city):
    # Ensure data directory exists
    os.makedirs(os.path.dirname(favorites_file), exist_ok=True)

    with open(favorites_file, "a") as f:
        f.write(f"{city}\n")

def show_favorites_window(root):
    fav_window = tk.Toplevel(root)
    fav_window.title("⭐ Favorite Cities")
    fav_window.geometry("350x350")
    fav_window.config(bg="#dfe6e9")

    title_label = tk.Label(fav_window, text="Your Favorite Cities", font=("Arial", 16, "bold"), bg="#dfe6e9")
    title_label.pack(pady=10)

    fav_listbox = tk.Listbox(fav_window, width=30, height=10, font=("Arial", 12))
    fav_listbox.pack(pady=10)

    # Load existing favorites if any
    if os.path.exists(favorites_file):
        with open(favorites_file, "r") as f:
            cities = f.readlines()
            if cities:
                for city in cities:
                    fav_listbox.insert(tk.END, city.strip())
            else:
                fav_listbox.insert(tk.END, "No favorites added yet.")
    else:
        fav_listbox.insert(tk.END, "No favorites added yet.")

    # --- Add new favorite city ---
    add_frame = tk.Frame(fav_window, bg="#dfe6e9")
    add_frame.pack(pady=5)

    new_city_entry = tk.Entry(add_frame, font=("Arial", 12), width=20)
    new_city_entry.pack(side=tk.LEFT, padx=5)

    def add_city():
        city = new_city_entry.get().strip()
        if city:
            add_favorite(city)
            fav_listbox.insert(tk.END, city)
            new_city_entry.delete(0, tk.END)

    add_btn = tk.Button(add_frame, text="Add Favorite", font=("Arial", 12), bg="#55efc4", command=add_city)
    add_btn.pack(side=tk.LEFT)

    # Allow pressing Enter to add favorite
    new_city_entry.bind("<Return>", lambda event: add_city())

    close_btn = tk.Button(fav_window, text="Close", font=("Arial", 12), bg="#fab1a0", command=fav_window.destroy)
    close_btn.pack(pady=10)

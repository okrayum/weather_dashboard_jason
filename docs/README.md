# Jason's Weather Dashboard

A Python Tkinter app that fetches weather data from OpenWeatherMap API, tracks weather history, displays temperature graphs, manages favorite cities, and features a fun weather mascot.

## Features

- **Weather History Tracker**: Saves daily weather data to CSV and shows last 7 days.
- **Temperature Graph**: Displays a matplotlib line graph of temperature trends.
- **Favorite Cities**: Save and quickly access preferred cities.
- **Mascot**: Reacts visually to current weather conditions.

## Setup

1. Clone the repo.

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash  
   pip install -r requirements.txt
   ```  

4. Set your OpenWeatherMap API key in `config.py`.

5. Run the app:

   ```bash
   python main.py
   ```

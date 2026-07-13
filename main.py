import tkinter as tk
from tkinter import messagebox
import requests
import datetime

# ---------------------------- CONFIGURATION & STYLE ------------------------------- #
BACKGROUND_COLOR = "#1E293B"  # Deep slate gray
CARD_COLOR = "#0F172A"  # Darker midnight blue for stats
TEXT_PRIMARY = "#F8FAFC"  # Clean white
ACCENT_BLUE = "#38BDF8"  # Bright sky blue for coordinates
ACCENT_GREEN = "#34D399"  # Emerald green for live status

FONT_TITLE = ("Helvetica", 18, "bold")
FONT_COORDS = ("Courier New", 24, "bold")
FONT_LABEL = ("Helvetica", 11, "normal")
FONT_STATUS = ("Helvetica", 10, "italic")

API_URL = "http://api.opennotify.org/iss-now.json"


# ---------------------------- REAL-TIME DATA FETCHING ----------------------------- #
def update_iss_location():
    try:
        # Fetch data from the live ISS API endpoint
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Parse coordinates and time metrics
        position = data["iss_position"]
        latitude = position["latitude"]
        longitude = position["longitude"]
        timestamp = data["timestamp"]

        # Convert Unix timestamp to readable local time format
        readable_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Update UI Elements smoothly
        lat_val_label.config(text=f"{latitude}°")
        lon_val_label.config(text=f"{longitude}°")
        time_val_label.config(text=f"Last Updated: {readable_time}")
        status_label.config(text="● Connection Live - Syncing Every 5s", fg=ACCENT_GREEN)

    except requests.exceptions.RequestException:
        # Soft-handle internet drops without crashing the UI application loop
        status_label.config(text="✕ Connection Error - Retrying...", fg="#F87171")

    # Schedule the next API query event loop sequence exactly 5000ms (5 seconds) later
    window.after(5000, update_iss_location)


# ---------------------------- UI INTERFACE WINDOW ------------------------------- #
window = tk.Tk()
window.title("ISS Real-Time Orbit Tracker")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
window.resizable(False, False)

# Header Title Block
title_label = tk.Label(text="INTERNATIONAL SPACE STATION", bg=BACKGROUND_COLOR, fg=TEXT_PRIMARY, font=FONT_TITLE)
title_label.pack(pady=(0, 5))

subtitle_label = tk.Label(text="Live Orbital Coordinates", bg=BACKGROUND_COLOR, fg=ACCENT_BLUE, font=FONT_LABEL)
subtitle_label.pack(pady=(0, 20))

# Display Card Layout Frame
stats_card = tk.Frame(window, bg=CARD_COLOR, bd=0, padx=25, pady=25)
stats_card.pack(fill="both", expand=True)

# Latitude Section
lat_title = tk.Label(stats_card, text="LATITUDE", bg=CARD_COLOR, fg="#94A3B8", font=FONT_LABEL)
lat_title.grid(row=0, column=0, sticky="w", pady=(0, 2))
lat_val_label = tk.Label(stats_card, text="0.0000°", bg=CARD_COLOR, fg=ACCENT_BLUE, font=FONT_COORDS)
lat_val_label.grid(row=1, column=0, sticky="w", padx=(0, 40), pady=(0, 20))

# Longitude Section
lon_title = tk.Label(stats_card, text="LONGITUDE", bg=CARD_COLOR, fg="#94A3B8", font=FONT_LABEL)
lon_title.grid(row=0, column=1, sticky="w", pady=(0, 2))
lon_val_label = tk.Label(stats_card, text="0.0000°", bg=CARD_COLOR, fg=ACCENT_BLUE, font=FONT_COORDS)
lon_val_label.grid(row=1, column=1, sticky="w", pady=(0, 20))

# Time Log Dashboard Row
time_val_label = tk.Label(stats_card, text="Connecting to satellite...", bg=CARD_COLOR, fg="#64748B", font=FONT_STATUS)
time_val_label.grid(row=2, column=0, columnspan=2, sticky="w")

# Bottom Network Connection Status Anchor
status_label = tk.Label(text="● Establishing API Handshake...", bg=BACKGROUND_COLOR, fg="#94A3B8", font=FONT_STATUS)
status_label.pack(pady=(20, 0))

# Trigger initial startup tracking task iteration immediately
update_iss_location()

window.mainloop()
import os
import tkinter as tk
from tkinter import messagebox

# --- CONFIGURATION & SAVING ---
SAVE_FILE = "habit_data.txt"
DAYS_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Supports leap years
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Design Colors
COLOR_INCOMPLETE = "#F0F0F0"  # Light gray pixel
COLOR_COMPLETE = "#1E1E1E"  # Dark "lit up" pixel
COLOR_BG = "#FFFFFF"


class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yearly Habit Tracker Pixel Grid")
        self.root.configure(bg=COLOR_BG)

        # Dictionary to store the state of each day: "Month_Day" -> True/False
        self.habit_data = self.load_data()

        self.create_grid_layout()

    def load_data(self):
        """Loads tracking data from a local file."""
        data = {}
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as file:
                    for line in file:
                        key, val = line.strip().split(":")
                        data[key] = val == "True"
            except Exception:
                messagebox.showwarning("Warning", "Could not load save file. Starting fresh!")
        return data

    def save_data(self):
        """Saves current tracking state to a local file."""
        try:
            with open(SAVE_FILE, "w") as file:
                for key, val in self.habit_data.items():
                    file.write(f"{key}:{val}\n")
        except Exception as e:
            print(f"Error saving data: {e}")

    def toggle_pixel(self, button, day_key):
        """Switches pixel color state and saves progress on click."""
        # Toggle boolean state
        is_complete = not self.habit_data.get(day_key, False)
        self.habit_data[day_key] = is_complete

        # Update UI visually
        if is_complete:
            button.configure(bg=COLOR_COMPLETE, activebackground=COLOR_COMPLETE)
        else:
            button.configure(bg=COLOR_INCOMPLETE, activebackground=COLOR_INCOMPLETE)

        self.save_data()

    def create_grid_layout(self):
        """Dynamically structures the 12x31 layout grid."""
        # Main container frame
        grid_frame = tk.Frame(self.root, bg=COLOR_BG, padx=15, pady=15)
        grid_frame.pack()

        # Render Month Headers (Columns)
        for col_idx, month in enumerate(MONTH_NAMES):
            header = tk.Label(
                grid_frame,
                text=month,
                font=("Arial", 10, "bold"),
                bg=COLOR_BG,
                fg="#333333",
                pady=5
            )
            header.grid(row=0, column=col_idx + 1, padx=2)

        # Render Day Row Numbers (1 to 31)
        for row_idx in range(1, 32):
            row_label = tk.Label(
                grid_frame,
                text=f"{row_idx:02d}",
                font=("Arial", 8),
                bg=COLOR_BG,
                fg="#888888",
                padx=5
            )
            row_label.grid(row=row_idx, column=0, sticky="e")

        # Build out individual Pixel Buttons
        for col_idx in range(12):
            max_days = DAYS_IN_MONTH[col_idx]

            for row_idx in range(1, 32):
                day_key = f"{col_idx + 1}_{row_idx}"

                # If the day doesn't exist in that specific month (e.g., Feb 30), leave it blank
                if row_idx > max_days:
                    blank_space = tk.Frame(grid_frame, width=24, height=20, bg=COLOR_BG)
                    blank_space.grid(row=row_idx, column=col_idx + 1, padx=2, pady=2)
                    continue

                # Determine initial visual color state based on loaded memory file
                already_done = self.habit_data.get(day_key, False)
                current_bg = COLOR_COMPLETE if already_done else COLOR_INCOMPLETE

                # Construct pixel button block
                pixel_btn = tk.Button(
                    grid_frame,
                    bg=current_bg,
                    activebackground=current_bg,
                    width=3,
                    height=1,
                    relief="flat",
                    bd=0
                )

                # Bind the click action using a lambda wrapper
                pixel_btn.configure(
                    command=lambda b=pixel_btn, k=day_key: self.toggle_pixel(b, k)
                )
                pixel_btn.grid(row=row_idx, column=col_idx + 1, padx=2, pady=2)


if __name__ == "__main__":
    window = tk.Tk()
    app = HabitTrackerApp(window)
    window.mainloop()
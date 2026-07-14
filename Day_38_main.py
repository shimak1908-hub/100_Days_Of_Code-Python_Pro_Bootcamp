import os
from datetime import datetime
import customtkinter as ctk

# --- UI Styling Theme Settings ---
ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

SAVE_FILE = "workout_history.txt"


class ModernFitnessTracker(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Level Up - Fitness Tracker")
        self.geometry("850x550")
        self.resizable(False, False)

        # Application State Data
        self.workouts = self.load_workouts()

        # Build UI Layout
        self.create_sidebar()
        self.create_main_dashboard()
        self.update_dashboard_stats()

    def load_workouts(self):
        """Loads logged exercise history from a text file."""
        workout_list = []
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as file:
                    for line in file:
                        parts = line.strip().split("|")
                        if len(parts) == 4:
                            workout_list.append(
                                {
                                    "date": parts[0],
                                    "type": parts[1],
                                    "duration": parts[2],
                                    "notes": parts[3],
                                }
                            )
            except Exception as e:
                print(f"Error loading workout data: {e}")
        return workout_list

    def save_workout_to_file(self, date, ex_type, duration, notes):
        """Appends a new workout directly onto the flat data file."""
        try:
            with open(SAVE_FILE, "a") as file:
                file.write(f"{date}|{ex_type}|{duration}|{notes}\n")
        except Exception as e:
            print(f"Error saving workout data: {e}")

    def create_sidebar(self):
        """Constructs the left-hand input form panel."""
        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        sidebar.pack(side="left", fill="y", padx=0, pady=0)

        # Title Logo
        logo = ctk.CTkLabel(
            sidebar, text="LEVEL UP", font=ctk.CTkFont(size=24, weight="bold")
        )
        logo.pack(padx=20, pady=(30, 40))

        # Exercise Type Dropdown Menu
        label_type = ctk.CTkLabel(
            sidebar, text="Exercise Type", anchor="w", font=ctk.CTkFont(size=13)
        )
        label_type.pack(fill="x", padx=25, pady=(0, 5))

        self.input_type = ctk.CTkOptionMenu(
            sidebar,
            values=[
                "Push-ups",
                "Cardio / Running",
                "Weight Training",
                "Calisthenics",
                "Yoga / Stretching",
            ],
        )
        self.input_type.pack(fill="x", padx=25, pady=(0, 20))

        # Duration Entry Field
        label_dur = ctk.CTkLabel(
            sidebar,
            text="Duration / Reps (e.g., 30 mins, 50 reps)",
            anchor="w",
            font=ctk.CTkFont(size=13),
        )
        label_dur.pack(fill="x", padx=25, pady=(0, 5))

        self.input_duration = ctk.CTkEntry(
            sidebar, placeholder_text="Enter value..."
        )
        self.input_duration.pack(fill="x", padx=25, pady=(0, 20))

        # Short Note Entry Field
        label_note = ctk.CTkLabel(
            sidebar,
            text="Quick Notes",
            anchor="w",
            font=ctk.CTkFont(size=13),
        )
        label_note.pack(fill="x", padx=25, pady=(0, 5))

        self.input_notes = ctk.CTkEntry(
            sidebar, placeholder_text="How did it feel?"
        )
        self.input_notes.pack(fill="x", padx=25, pady=(0, 30))

        # Submission Log Button
        btn_log = ctk.CTkButton(
            sidebar,
            text="Log Workout",
            font=ctk.CTkFont(weight="bold"),
            command=self.log_workout,
        )
        btn_log.pack(fill="x", padx=25, pady=0)

    def create_main_dashboard(self):
        """Establishes the right-hand layout dashboard visualization frames."""
        self.main_content = ctk.CTkFrame(
            self, fg_color="transparent", corner_radius=0
        )
        self.main_content.pack(side="right", fill="both", expand=True, padx=25, pady=25)

        # --- STAT CARDS ROW ---
        self.stats_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))

        # Total Workouts Counter Card
        self.card_total = ctk.CTkFrame(self.stats_frame, height=100)
        self.card_total.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.lbl_total_title = ctk.CTkLabel(
            self.card_total,
            text="Total Workouts",
            font=ctk.CTkFont(size=12, text_color="gray"),
        )
        self.lbl_total_title.pack(pady=(15, 2))
        self.lbl_total_val = ctk.CTkLabel(
            self.card_total, text="0", font=ctk.CTkFont(size=28, weight="bold")
        )
        self.lbl_total_val.pack(pady=(0, 15))

        # Recent Activity Summary Card
        self.card_recent = ctk.CTkFrame(self.stats_frame, height=100)
        self.card_recent.pack(side="right", fill="both", expand=True, padx=(10, 0))
        self.lbl_recent_title = ctk.CTkLabel(
            self.card_recent,
            text="Most Frequent Habit",
            font=ctk.CTkFont(size=12, text_color="gray"),
        )
        self.lbl_recent_title.pack(pady=(15, 2))
        self.lbl_recent_val = ctk.CTkLabel(
            self.card_recent, text="None", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.lbl_recent_val.pack(pady=(5, 15))

        # --- HISTORY LOG PANEL ---
        lbl_history = ctk.CTkLabel(
            self.main_content,
            text="Activity History Log",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
        )
        lbl_history.pack(fill="x", pady=(10, 5))

        # Scrollable Box Container for long transaction lists
        self.scroll_history = ctk.CTkScrollableFrame(
            self.main_content, label_text=""
        )
        self.scroll_history.pack(fill="both", expand=True)

        # Initial loading display population
        self.populate_history_view()

    def log_workout(self):
        """Extracts field data, saves it locally, and refreshes the UI."""
        ex_type = self.input_type.get()
        duration = self.input_duration.get().strip()
        notes = self.input_notes.get().strip()

        # Simple data presence fallback validation
        if not duration:
            duration = "Completed"
        if not notes:
            notes = "No extra notes recorded."

        today_date = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Update program dynamic dictionary arrays
        self.workouts.append(
            {"date": today_date, "type": ex_type, "duration": duration, "notes": notes}
        )

        # Permanent text file logging output
        self.save_workout_to_file(today_date, ex_type, duration, notes)

        # Reset text entries safely
        self.input_duration.delete(0, "end")
        self.input_notes.delete(0, "end")

        # Force structural window visual update refreshes
        self.populate_history_view()
        self.update_dashboard_stats()

    def populate_history_view(self):
        """Clears out the scrolling panel and rebuilds the rows in reverse chronological order."""
        for child in self.scroll_history.winfo_children():
            child.destroy()

        # Render list backward so freshest records sit neatly at the top top row
        for item in reversed(self.workouts):
            row = ctk.CTkFrame(self.scroll_history, fg_color=["#EAEAEA", "#2B2B2B"], pady=8)
            row.pack(fill="x", pady=4, padx=5)

            # Metadata Display Labels Arrangement
            lbl_meta = ctk.CTkLabel(
                row,
                text=f"🗓️ {item['date']}  |  💪 {item['type']} ({item['duration']})",
                font=ctk.CTkFont(weight="bold", size=13),
                anchor="w",
            )
            lbl_meta.pack(fill="x", padx=15)

            lbl_desc = ctk.CTkLabel(
                row,
                text=item["notes"],
                font=ctk.CTkFont(size=12, slant="italic"),
                text_color="gray",
                anchor="w",
            )
            lbl_desc.pack(fill="x", padx=15, pady=(2, 0))

    def update_dashboard_stats(self):
        """Recalculates frequency counts to update the display cards."""
        total_count = len(self.workouts)
        self.lbl_total_val.configure(text=str(total_count))

        if total_count > 0:
            # Frequency count calculation
            type_tallies = {}
            for w in self.workouts:
                type_tallies[w["type"]] = type_tallies.get(w["type"], 0) + 1
            favorite_habit = max(type_tallies, key=type_tallies.get)
            self.lbl_recent_val.configure(text=f"{favorite_habit} ({type_tallies[favorite_habit]}x)")
        else:
            self.lbl_recent_val.configure(text="None Recorded")


if __name__ == "__main__":
    app = ModernFitnessTracker()
    app.mainloop()
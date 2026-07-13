import tkinter as tk
from tkinter import messagebox
import requests
import html

# ---------------------------- CONFIGURATION & STYLING ------------------------- #
THEME_BG = "#212529"  # Dark gray background
CARD_BG = "#FFFFFF"  # Crisp white card for the question face
TEXT_DARK = "#343A40"  # Dark charcoal for readability
SCORE_COLOR = "#F8F9FA"  # Light gray for text visibility
COLOR_CORRECT = "#2ECC71"  # Emerald green flash
COLOR_WRONG = "#E74C3C"  # Vivid crimson flash

FONT_SCORE = ("Helvetica", 12, "bold")
FONT_QUESTION = ("Arial", 16, "italic")


# ---------------------------- QUIZ LOGIC INTERFACE ---------------------------- #
class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler Live!")
        self.window.config(padx=20, pady=20, bg=THEME_BG)
        self.window.resizable(False, False)

        # State Data Parameters
        self.score = 0
        self.question_number = 0
        self.questions_list = []
        self.current_question_answer = ""

        # UI Setup Components
        self.score_label = tk.Label(text="Score: 0/10", fg=SCORE_COLOR, bg=THEME_BG, font=FONT_SCORE)
        self.score_label.grid(row=0, column=1, sticky="ne", pady=(0, 20))

        self.canvas = tk.Canvas(width=340, height=260, bg=CARD_BG, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            170, 130,
            text="Fetching questions from satellite database...",
            width=300,
            fill=TEXT_DARK,
            font=FONT_QUESTION,
            justify="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 30))

        # Modern Flat Action Control Buttons
        self.true_btn = tk.Button(
            text="✓ TRUE", font=("Helvetica", 12, "bold"), bg="#4D96FF", fg="white",
            activebackground="#3b76cc", activeforeground="white",
            width=10, height=2, bd=0, cursor="hand2", command=self.pressed_true
        )
        self.true_btn.grid(row=2, column=0, padx=10)
        self.true_btn.config(state="disabled")  # Disabled until live API content arrives

        self.false_btn = tk.Button(
            text="✕ FALSE", font=("Helvetica", 12, "bold"), bg="#FF6B6B", fg="white",
            activebackground="#cc5555", activeforeground="white",
            width=10, height=2, bd=0, cursor="hand2", command=self.pressed_false
        )
        self.false_btn.grid(row=2, column=1, padx=10)
        self.false_btn.config(state="disabled")

        # Initialize Remote Data Download
        self.fetch_trivia_questions()

        self.window.mainloop()

    def fetch_trivia_questions(self):
        """Fetches 10 fresh True/False questions dynamically via OpenTDb API."""
        url = "https://opentdb.com/api.php?amount=10&type=boolean"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data["response_code"] == 0:
                self.questions_list = data["results"]
                # Enable controls and draw the first question
                self.true_btn.config(state="normal")
                self.false_btn.config(state="normal")
                self.get_next_question()
            else:
                self.canvas.itemconfig(self.question_text, text="Error gathering pool data. Please restart.")
        except requests.exceptions.RequestException:
            self.canvas.itemconfig(self.question_text, text="Network Timeout! Check your connection parameters.")

    def get_next_question(self):
        """Advances the queue layout or ends the execution sequence when out of questions."""
        self.canvas.config(bg=CARD_BG)  # Reset background card color frame

        if self.question_number < len(self.questions_list):
            # Update Score Metadata Display
            self.score_label.config(text=f"Score: {self.score}/{len(self.questions_list)}")

            # Fetch current row dictionary target data structural blocks
            q_data = self.questions_list[self.question_number]
            self.current_question_answer = q_data["correct_answer"]

            # Extract and unescape raw text content from JSON fields safely
            raw_q_text = q_data["question"]
            clean_q_text = html.unescape(raw_q_text)

            self.question_number += 1
            self.canvas.itemconfig(self.question_text, text=f"Q.{self.question_number}: {clean_q_text}")
        else:
            # End of structural index path reached
            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed!\n\nFinal Score: {self.score}/10")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            messagebox.showinfo(title="Quiz Over", message=f"You completed the deck!\nFinal Score: {self.score}/10")

    def pressed_true(self):
        self.check_answer("True")

    def pressed_false(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        """Validates matches and provides an instantaneous interactive feedback color flash."""
        is_correct = user_answer == self.current_question_answer

        if is_correct:
            self.score += 1
            self.canvas.config(bg=COLOR_CORRECT)
        else:
            self.canvas.config(bg=COLOR_WRONG)

        # Freeze action elements during visual presentation feedback window
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")

        # Schedule canvas normalization routine 1000 milliseconds later
        self.window.after(1000, self.reactivate_and_continue)

    def reactivate_and_continue(self):
        """Restores key elements and steps down the loop pipeline execution."""
        self.true_btn.config(state="normal")
        self.false_btn.config(state="normal")
        self.get_next_question()


# ---------------------------- RUNTIME CONTROLLER ------------------------------ #
if __name__ == "__main__":
    QuizInterface()
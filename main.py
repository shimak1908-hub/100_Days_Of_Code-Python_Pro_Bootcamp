from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- COLOR PALETTE & CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#F4F6F9"
CARD_FRONT_COLOR = "#FFFFFF"
CARD_BACK_COLOR = "#2C3E50"
TEXT_DARK = "#333333"
TEXT_LIGHT = "#FFFFFF"
ACCENT_BLUE = "#3498DB"
ACCENT_GREEN = "#2ECC71"
ACCENT_RED = "#E74C3C"

FONT_KANJI = ("Helvetica", 70, "bold")
FONT_LABEL = ("Helvetica", 12, "normal")
FONT_MEANING = ("Helvetica", 24, "bold")
FONT_STATS = ("Helvetica", 14, "bold")

# ---------------------------- KANJI DATA DATASET ------------------------------- #
KANJI_DATASET = [
    {"kanji": "一", "meaning": "One", "onyomi": "イチ", "kunyomi": "ひと-つ"},
    {"kanji": "二", "meaning": "Two", "onyomi": "ニ", "kunyomi": "ふた-つ"},
    {"kanji": "三", "meaning": "Three", "onyomi": "サン", "kunyomi": "みっ-つ"},
    {"kanji": "四", "meaning": "Four", "onyomi": "シ", "kunyomi": "よっ-つ"},
    {"kanji": "五", "meaning": "Five", "onyomi": "ゴ", "kunyomi": "いつ-つ"},
    {"kanji": "六", "meaning": "Six", "onyomi": "ロク", "kunyomi": "むっ-つ"},
    {"kanji": "七", "meaning": "Seven", "onyomi": "シチ", "kunyomi": "なな-つ"},
    {"kanji": "八", "meaning": "Eight", "onyomi": "ハチ", "kunyomi": "よう-つ"},
    {"kanji": "九", "meaning": "Nine", "onyomi": "キュウ", "kunyomi": "ここの-つ"},
    {"kanji": "十", "meaning": "Ten", "onyomi": "ジュウ", "kunyomi": "とお"},
    {"kanji": "日", "meaning": "Day / Sun", "onyomi": "ニチ", "kunyomi": "ひ"},
    {"kanji": "本", "meaning": "Book / Origin", "onyomi": "ホン", "kunyomi": "moto"},
    {"kanji": "人", "meaning": "Person", "onyomi": "ジン / ニン", "kunyomi": "hito"},
    {"kanji": "月", "meaning": "Moon / Month", "onyomi": "ゲツ / ガツ", "kunyomi": "tsuki"},
    {"kanji": "火", "meaning": "Fire", "onyomi": "カ", "kunyomi": "hi"},
    {"kanji": "水", "meaning": "Water", "onyomi": "スイ", "kunyomi": "mizu"},
    {"kanji": "木", "meaning": "Tree / Wood", "onyomi": "モク", "kunyomi": "ki"},
    {"kanji": "金", "meaning": "Gold / Money", "onyomi": "キン", "kunyomi": "kane"},
    {"kanji": "土", "meaning": "Earth / Soil", "onyomi": "ド", "kunyomi": "tsuchi"},
]

# ---------------------------- APP STATE & LOGIC ------------------------------- #
current_card = {}
score = 0
is_flipped = False


def next_card():
    global current_card, is_flipped
    is_flipped = False
    current_card = random.choice(KANJI_DATASET)

    # Reset Card Background
    card_canvas.config(bg=CARD_FRONT_COLOR)

    # FIXED: Using card_canvas.itemconfig() for elements inside the canvas
    card_canvas.itemconfig(card_title, text="Kanji", fill=ACCENT_BLUE)
    card_canvas.itemconfig(card_main, text=current_card["kanji"], font=FONT_KANJI, fill=TEXT_DARK)
    card_canvas.itemconfig(card_sub, text="Click Card to Flip & Reveal Meaning", fill="#7F8C8D",
                           font=("Helvetica", 10, "italic"))


def flip_card(event=None):
    global is_flipped
    if not is_flipped:
        is_flipped = True
        card_canvas.config(bg=CARD_BACK_COLOR)

        details = f"{current_card['meaning']}\n\n" \
                  f"Onyomi: {current_card['onyomi']}\n" \
                  f"Kunyomi: {current_card['kunyomi']}"

        # FIXED: Using card_canvas.itemconfig() for elements inside the canvas
        card_canvas.itemconfig(card_title, text="Meaning & Readings", fill=ACCENT_GREEN)
        card_canvas.itemconfig(card_main, text=details, font=FONT_MEANING, fill=TEXT_LIGHT)
        card_canvas.itemconfig(card_sub, text="Mark 'Correct' or 'Wrong' below", fill="#BDC3C7",
                               font=("Helvetica", 10, "italic"))


def mark_correct():
    global score
    if not is_flipped:
        flip_card()
        return
    score += 1
    score_label.config(text=f"Score: {score}")
    next_card()


def mark_wrong():
    if not is_flipped:
        flip_card()
        return
    next_card()


# ---------------------------- UI INTERFACE WINDOW ------------------------------- #
window = Tk()
window.title("Level Up Kanji Study Flashcards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
window.resizable(False, False)

# Score Dashboard Header
score_label = Label(text=f"Score: {score}", bg=BACKGROUND_COLOR, fg=TEXT_DARK, font=FONT_STATS)
score_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))

# Flat Interactive Canvas Card UI
card_canvas = Canvas(width=450, height=300, bg=CARD_FRONT_COLOR, highlightthickness=0, bd=0)
card_canvas.bind("<Button-1>", flip_card)
card_canvas.grid(row=1, column=0, columnspan=2, pady=(0, 30))

# Canvas Text Alignments (These return integer IDs)
card_title = card_canvas.create_text(225, 45, text="", font=FONT_LABEL)
card_main = card_canvas.create_text(225, 140, text="", font=FONT_KANJI, justify="center")
card_sub = card_canvas.create_text(225, 260, text="", font=FONT_LABEL)

# Control Buttons
wrong_btn = Button(
    text="✕ Wrong",
    font=FONT_LABEL,
    bg=ACCENT_RED,
    fg=TEXT_LIGHT,
    activebackground="#C0392B",
    activeforeground=TEXT_LIGHT,
    width=12,
    height=2,
    bd=0,
    cursor="hand2",
    command=mark_wrong
)
wrong_btn.grid(row=2, column=0, padx=10)

correct_btn = Button(
    text="✓ Correct",
    font=FONT_LABEL,
    bg=ACCENT_GREEN,
    fg=TEXT_LIGHT,
    activebackground="#27AE60",
    activeforeground=TEXT_LIGHT,
    width=12,
    height=2,
    bd=0,
    cursor="hand2",
    command=mark_correct
)
correct_btn.grid(row=2, column=1, padx=10)

# Initialize Program Framework State
next_card()

window.mainloop()
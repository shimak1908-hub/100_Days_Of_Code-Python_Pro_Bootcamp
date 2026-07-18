import random
from flask import Flask

app = Flask(__name__)

# Generate a target number between 0 and 9 inclusive on server startup
TARGET_NUMBER = random.randint(0, 9)
print(f"[System Setup] Target answer calculated for this runtime session: {TARGET_NUMBER}")


@app.route("/")
def home():
    """Renders the main landing screen instruction set."""
    return (
        "<h1>Guess a number between 0 and 9!</h1>"
        "<p>Type your guess directly into the URL bar above! For example: <b>/5</b></p>"
        "<img src='https://media.giphy.com/media/3o7aCSPYUPtPk6v1cY/giphy.gif' width='400' alt='Numbers floating'>"
    )


# <int:guess> parses the trailing URL element, forces integer type conversion,
# and safely passes the variable directly into our controller function.
@app.route("/<int:guess>")
def check_guess(guess):
    """Parses URL segment parameters and renders higher, lower, or correct feedback states."""
    if guess < TARGET_NUMBER:
        return (
            "<h1 style='color: #e74c3c;'>Too low, try again!</h1>"
            f"<p>Your guess: {guess}</p>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='400' alt='Too low cartoon'>"
        )

    elif guess > TARGET_NUMBER:
        return (
            "<h1 style='color: #3498db;'>Too high, try again!</h1>"
            f"<p>Your guess: {guess}</p>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='400' alt='Too high cartoon'>"
        )

    else:
        return (
            "<h1 style='color: #2ecc71;'>You found me! Excellent guess!</h1>"
            f"<p>The correct answer was indeed {guess}!</p>"
            "<img src='https://media.giphy.com/media/4T7eWG7jR32AMwMHfL/giphy.gif' width='400' alt='Success celebration'>"
        )


if __name__ == "__main__":
    # debug=True auto-reloads your backend logic whenever you hit save
    app.run(debug=True)
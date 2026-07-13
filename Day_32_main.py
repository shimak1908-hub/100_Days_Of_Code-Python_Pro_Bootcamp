import smtplib
import datetime as dt
import pandas as pd
from email.message import EmailMessage

# ---------------------------- CONFIGURATION ------------------------------- #
# Update these details with your active email provider configuration
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"  # Use an App Password here, NOT your login password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ---------------------------- CHECK BIRTHDAYS ------------------------------- #
# 1. Grab today's current tracking month and day metrics
now = dt.datetime.now()
today_month = now.month
today_day = now.day

try:
    # 2. Read spreadsheet file into a dynamic DataFrame data structure
    df = pd.read_excel("birthdays.xlsx")

    # Filter columns matching today's month and day combos
    matching_birthdays = df[(df["birth_month"] == today_month) & (df["birth_day"] == today_day)]

    # 3. Process records if any rows return matching profiles
    if not matching_birthdays.empty:
        # Connect to the mail transfer protocol system
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()  # Secure the connection profile
            connection.login(MY_EMAIL, MY_PASSWORD)

            # Iterate through each person matching today's criteria
            for index, row in matching_birthdays.iterrows():
                recipient_name = row["name"]
                recipient_email = row["email"]

                # Compose the Email Context Structure
                msg = EmailMessage()
                msg["Subject"] = "Happy Birthday! 🎂🎉"
                msg["From"] = MY_EMAIL
                msg["To"] = recipient_email

                # Custom personalized message block
                body_content = f"Hello {recipient_name},\n\nWishing you a very Happy Birthday! Hope you have an amazing day ahead and a fantastic year to come.\n\nBest regards,\n[Your Name]"
                msg.set_content(body_content)

                # Send the message
                connection.send_message(msg)
                print(f"Success: Birthday wish sent to {recipient_name} ({recipient_email})!")

    else:
        print("No birthdays found matching today's date structure.")

except FileNotFoundError:
    print("Error: The 'birthdays.xlsx' data file was not found in the project path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
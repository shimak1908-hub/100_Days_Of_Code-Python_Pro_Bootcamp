from tkinter import *
from tkinter import messagebox
import random
import json  # Added to read and write JSON data


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()  # standardizing case for reliable matching

    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter a website to search.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found. Save a password first!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [random.choice(letters) for _ in range(8)]
    password_list += [random.choice(symbols) for _ in range(2)]
    password_list += [random.choice(numbers) for _ in range(2)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    # Formatting structure for JSON
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # 1. Try reading existing file data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # 2. If it doesn't exist, start fresh with current data
            data = new_data
        else:
            # 3. If file exists, update old dictionary with new data
            data.update(new_data)

        # 4. Save the updated layout back into the file
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except:
    pass
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)  # Adjusted width to accommodate search button cleanly
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "common_email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(row=1, column=2)
gen_pass_button = Button(text="Generate Password", width=11, command=generate_password)
gen_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_box.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for b in range(nr_symbols)]
    password_list += [random.choice(numbers) for c in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_box.get()
    email_data = email_box.get()
    password_data = password_box.get()

    if website_data == "" or password_data == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the details entered: \nEmail: {email_data} "
                                               f"\nPassword: {password_data} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_box.delete(0, "end")
                password_box.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_title = Label(text="Website:")
website_title.grid(column=0, row=1)

username_title = Label(text="Email/Username:")
username_title.grid(column=0, row=2)

password_title = Label(text="Password:")
password_title.grid(column=0, row=3)

# Entries
website_box = Entry()
website_box.grid(column=1, row=1, columnspan=2, sticky="EW")
# website_box.focus()

email_box = Entry()
email_box.grid(column=1, row=2, columnspan=2, sticky="EW")
email_box.insert(0, "hahaha@email.com")

password_box = Entry()
password_box.grid(column=1, row=3, sticky="EW")
password_box.focus()

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

# Installation for Tkinter in README.md
import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password():
    capital_letter = random.choice(string.ascii_uppercase)
    lowercase_letters = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
    numbers = "".join(random.choice(string.digits) for _ in range(5))
    generated_password = capital_letter + lowercase_letters + numbers
    password_var.set(generated_password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    
    copied_var.set("Copied to Clipboard!")
    root.after(5000, lambda: copied_var.set(""))


# Create the main window
root = tk.Tk()
root.title("Password Generator")


# Variable to store the generated password
password_var = tk.StringVar()

# Create GUI elements
label = ttk.Label(root, text="Generated Password:")
label.grid(row=0, column=0, padx=10, pady=10)

password_entry = ttk.Entry(root, textvariable=password_var, state="readonly")
password_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=2, column=0, columnspan=2, pady=10)

copied_var = tk.StringVar()
copied_var.set("")
copied = ttk.Label(root, textvariable=copied_var)
copied.grid(row=3, column=0, columnspan=2, pady=10)


# Run the Tkinter event loop
root.mainloop()
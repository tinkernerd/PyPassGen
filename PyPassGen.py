import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password():
    """Generates a password based on user selections."""
    length = length_var.get() if length_check_var.get() else 12
    easier_to_communicate = easy_to_communicate_var.get()

    if easier_to_communicate:
        half_length = length // 2

        # First half: First letter capital, rest lowercase
        first_half = random.choice(string.ascii_uppercase) + "".join(random.choice(string.ascii_lowercase) for _ in range(half_length - 1))

        # Second half: Mix of numbers and special characters
        second_half_chars = string.digits + string.punctuation
        second_half = "".join(random.choice(second_half_chars) for _ in range(length - half_length))

        generated_password = first_half + second_half
    else:
        char_pool = string.ascii_lowercase
        if capital_var.get():
            char_pool += string.ascii_uppercase
        if numbers_var.get():
            char_pool += string.digits
        if punctuation_var.get():
            char_pool += string.punctuation

        generated_password = "".join(random.choice(char_pool) for _ in range(length))

    password_var.set(generated_password)


def copy_to_clipboard():
    """Copies the generated password to clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    
    copied_var.set("Copied to Clipboard!")
    root.after(5000, lambda: copied_var.set(""))


def toggle_options():
    """Disables or enables options based on 'Easier to Communicate' checkbox."""
    state = tk.DISABLED if easy_to_communicate_var.get() else tk.NORMAL
    capital_check.config(state=state)
    punctuation_check.config(state=state)
    numbers_check.config(state=state)


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Variables for options
password_var = tk.StringVar()
copied_var = tk.StringVar()
copied_var.set("")
length_var = tk.IntVar(value=12)
length_check_var = tk.BooleanVar()
easy_to_communicate_var = tk.BooleanVar()
capital_var = tk.BooleanVar()
punctuation_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()

# Layout
options_frame = ttk.LabelFrame(root, text="Options")
options_frame.grid(row=0, column=0, padx=10, pady=10, rowspan=4, sticky="nw")

# Checkboxes for options
length_check = ttk.Checkbutton(options_frame, text="Password Length:", variable=length_check_var)
length_check.grid(row=0, column=0, sticky="w")
length_entry = ttk.Entry(options_frame, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=5)

easy_to_communicate_check = ttk.Checkbutton(
    options_frame, text="Easier to Com.", variable=easy_to_communicate_var, command=toggle_options
)
easy_to_communicate_check.grid(row=1, column=0, columnspan=2, sticky="w")

capital_check = ttk.Checkbutton(options_frame, text="Capital Letters", variable=capital_var)
capital_check.grid(row=2, column=0, columnspan=2, sticky="w")

punctuation_check = ttk.Checkbutton(options_frame, text="Punctuation (Special Chars)", variable=punctuation_var)
punctuation_check.grid(row=3, column=0, columnspan=2, sticky="w")

numbers_check = ttk.Checkbutton(options_frame, text="Numbers", variable=numbers_var)
numbers_check.grid(row=4, column=0, columnspan=2, sticky="w")

# Password display and buttons
password_label = ttk.Label(root, text="Generated Password:")
password_label.grid(row=0, column=1, padx=10, pady=10)

password_entry = ttk.Entry(root, textvariable=password_var, state="readonly", width=30)
password_entry.grid(row=0, column=2, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=1, columnspan=2, pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=2, column=1, columnspan=2, pady=10)

copied = ttk.Label(root, textvariable=copied_var)
copied.grid(row=3, column=1, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

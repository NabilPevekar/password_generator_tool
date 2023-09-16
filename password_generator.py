import string
import random
import tkinter as tk
from tkinter import ttk
import pyperclip


def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    """Generates a random password of a specified length and character set."""

    # Create a list of all possible characters.
    characters = []
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_lowercase:
        characters.extend(string.ascii_lowercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_symbols:
        characters.extend(string.punctuation)

    # Generate a random password.
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def generate_button_clicked():
    """Event handler for the Generate Password button."""
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get() == 1
    include_lowercase = lowercase_var.get() == 1
    include_numbers = numbers_var.get() == 1
    include_symbols = symbols_var.get() == 1

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)

    password_output.delete(0, tk.END)
    password_output.insert(0, password)


def copy_button_clicked():
    """Event handler for the Copy to Clipboard button."""
    password = password_output.get()
    pyperclip.copy(password)
    print("Password copied to clipboard.")


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure GUI components
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root)
length_entry.insert(0, "12")  # Default length
uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

uppercase_checkbox = ttk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
lowercase_checkbox = ttk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
numbers_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_button_clicked)
password_output = ttk.Entry(root)

# Place GUI components on the window
length_label.pack()
length_entry.pack()
uppercase_checkbox.pack()
lowercase_checkbox.pack()
numbers_checkbox.pack()
symbols_checkbox.pack()
generate_button.pack()
copy_button.pack()
password_output.pack()

# Start the main loop
root.mainloop()

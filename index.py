import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if not length.isdigit() or int(length) < 6:
        messagebox.showerror("Invalid Input", "Password length must be a number and at least 6.")
        return
    
    length = int(length)
    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    # Character pools
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    # Generate password
    password = ''.join(random.choices(char_pool, k=length))
    result_label.config(text=password)

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Update clipboard
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18))
title_label.pack(pady=10)

# Length input
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 14))
length_label.pack(pady=5)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Helvetica", 14), width=10)
length_entry.pack(pady=5)

# Options for character types
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=("Helvetica", 12))
uppercase_check.pack(pady=5)

lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, font=("Helvetica", 12))
lowercase_check.pack(pady=5)

digits_check = tk.Checkbutton(root, text="Include Numbers", variable=digits_var, font=("Helvetica", 12))
digits_check.pack(pady=5)

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Helvetica", 12))
special_check.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 14), command=generate_password)
generate_button.pack(pady=10)

# Password result
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 14), command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()

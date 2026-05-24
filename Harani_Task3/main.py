import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length")
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter numbers only")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

# Length
tk.Label(root, text="Password Length").pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Options
var_letters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Symbols", variable=var_symbols).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result
result_entry = tk.Entry(root, width=30)
result_entry.pack()

# Copy button
tk.Button(root, text="Copy", command=copy_password).pack(pady=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid positive values")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    except ValueError:
        messagebox.showerror("Error", "Enter numbers only")

# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Weight
tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

# Height
tk.Label(root, text="Height (m)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
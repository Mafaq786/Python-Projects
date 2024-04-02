import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birthdate_str = birthdate_entry.get()
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        messagebox.showinfo("Age Calculator", "You are {} years old.".format(age))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date in DD/MM/YYYY format.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Create entry box for birthdate
birthdate_label = tk.Label(root, text="Enter your birthdate (DD/MM/YYYY):")
birthdate_label.pack()
birthdate_entry = tk.Entry(root)
birthdate_entry.pack()

# Create button to calculate age
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

# Run the main event loop
root.mainloop()

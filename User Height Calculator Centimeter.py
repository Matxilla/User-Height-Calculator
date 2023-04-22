import tkinter as tk
from tkinter import messagebox

# Function to calculate and display height
def calculate_height():
    try:
        height = float(height_input.get())
        if height.is_integer():
            height_str = str(int(height))
        else:
            height_str = str(height)
        result = messagebox.showinfo("Result", f"Your height is {height_str}!")
        if result == "ok":
            root.destroy()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("User Height Calculator")

# Get screen dimensions and calculate window position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 250
window_height = 200
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

# Set window geometry
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Create label and text input box
height_label = tk.Label(root, text="Enter your height (in cm):")
height_label.pack()
height_input = tk.Entry(root)
height_input.pack()

# Bind the <Return> key to the calculate_height function
root.bind('<Return>', lambda event=None: calculate_height())

# Create the "Calculate" button
calculate_button = tk.Button(root, text="Calculate", command=calculate_height)
calculate_button.pack()

# Start the main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Define the expression variable
expression = ""

# Define functions for calculator operations
def append_to_expression(value):
    global expression
    expression += str(value)
    display_var.set(expression)  # Update the display

def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        display_var.set(result)  # Show the result in the display
        expression = result  # Set the result as the new expression
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        display_var.set("")

def clear_expression():
    global expression
    expression = ""
    display_var.set("")  # Clear the display

# Display (Entry) to show the expression and result
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create number and operator buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                        command=evaluate_expression)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                        command=lambda t=text: append_to_expression(t))
    btn.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_expression)
clear_button.grid(row=5, column=0, columnspan=4, sticky="we")

# Run the application
root.mainloop()

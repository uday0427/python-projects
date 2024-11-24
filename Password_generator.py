import tkinter as tk
import random
import string
import pyperclip  # For copying password to clipboard

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.config(bg='lightblue')  # Set background color of the window

# Define password generation function
def generate_password():
    length = int(length_var.get())  # Get the desired password length
    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    # Character sets based on the selected options
    char_set = ""
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    # Ensure at least one character set is selected
    if not char_set:
        password_var.set("Please select at least one character type!")
        return

    # Generate a random password using the selected character set
    password = ''.join(random.choice(char_set) for _ in range(length))
    password_var.set(password)  # Display the generated password

# Function to copy the generated password to clipboard
def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setup the UI elements
length_label = tk.Label(root, text="Password Length:", font=("Arial", 14), bg='lightblue')
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

length_var = tk.StringVar(value="12")  # Default length
length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 14), width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, font=("Arial", 12), bg='lightblue')
uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var, font=("Arial", 12), bg='lightblue')
lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=("Arial", 12), bg='lightblue')
digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 12), bg='lightblue')
special_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="blue", fg="white", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Display generated password
password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:", font=("Arial", 14), bg='lightblue')
password_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

password_display = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25, state="readonly", bg="white")
password_display.grid(row=6, column=1, padx=10, pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy", font=("Arial", 14), bg="green", fg="white", command=copy_password)
copy_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

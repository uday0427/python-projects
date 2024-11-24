import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Vibrant Contact Book")
root.geometry("900x650")
root.configure(bg="#FFFFFF")  # White background for a bright look

# Dictionary to store contact information
contacts = {}

# Function to add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts[name] = phone
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        view_contacts()  # Refresh contact list after adding
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone.")

# Function to view contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_list.insert(tk.END, f"{name}: {phone}")

# Function to delete a specific contact
def delete_contact():
    name = delete_entry.get()
    if name in contacts:
        del contacts[name]
        view_contacts()  # Refresh contact list after deleting
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        delete_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", f"No contact found with name '{name}'.")

# Title Label
title_label = tk.Label(root, text="Contact Book", font=("Helvetica Neue", 28, "bold"), fg="#283747", bg="#FFFFFF")
title_label.pack(pady=20)

# Frame for input fields and buttons with border and padding
input_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="ridge")
input_frame.pack(pady=20, padx=20, ipadx=10, ipady=10)

# Labels and Entries for Adding Contact
name_label = tk.Label(input_frame, text="Name:", font=("Helvetica Neue", 16), fg="#283747", bg="#FAD7A0")
name_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
name_entry = tk.Entry(input_frame, font=("Helvetica Neue", 14), width=30, bg="#FFF2E2", fg="#283747", insertbackground="#283747")
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(input_frame, text="Phone:", font=("Helvetica Neue", 16), fg="#283747", bg="#FAD7A0")
phone_label.grid(row=1, column=0, padx=5, pady=10, sticky="e")
phone_entry = tk.Entry(input_frame, font=("Helvetica Neue", 14), width=30, bg="#FFF2E2", fg="#283747", insertbackground="#283747")
phone_entry.grid(row=1, column=1, padx=10, pady=10)

# Function to create styled buttons
def create_button(text, color, command):
    return tk.Button(button_frame, text=text, font=("Helvetica Neue", 14, "bold"), bg=color, fg="white", 
                     width=14, height=2, command=command, relief="groove", bd=2)

# Buttons for adding, viewing, and deleting contacts with rounded edges and borders
button_frame = tk.Frame(root, bg="#FFFFFF")
button_frame.pack(pady=10)

add_button = create_button("Add Contact", "#4169E1", add_contact)
add_button.pack(side="left", padx=15)

view_button = create_button("View Contacts", "#28A745", view_contacts)
view_button.pack(side="left", padx=15)

# Frame and entry for deleting a specific contact by name
delete_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="ridge")
delete_frame.pack(pady=20, padx=20, ipadx=10, ipady=10)

delete_label = tk.Label(delete_frame, text="Delete by Name:", font=("Helvetica Neue", 16), fg="#283747", bg="#FFDAB9")
delete_label.pack(side="left", padx=5, pady=10)
delete_entry = tk.Entry(delete_frame, font=("Helvetica Neue", 14), width=20, bg="#FFF2E2", fg="#283747", insertbackground="#283747")
delete_entry.pack(side="left", padx=10, pady=10)

delete_button = tk.Button(delete_frame, text="Delete Contact", font=("Helvetica Neue", 14, "bold"), bg="#DC3545", fg="white", command=delete_contact)
delete_button.pack(side="left", padx=10)

# Contact List Display with bright colors and scrollbar
list_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="ridge") 
list_frame.pack(pady=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

contact_list = tk.Listbox(
    list_frame, font=("Helvetica Neue", 14), width=40, height=10, bg="#FDEDEC", fg="#283747", 
    yscrollcommand=scrollbar.set, selectbackground="#FF6F61", selectforeground="white"
)
contact_list.pack(side="left", fill="both")
scrollbar.config(command=contact_list.yview)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Create a list to store tasks
tasks = []

# Define functions for task management
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)  # Add to the Listbox
        tasks.append(task)  # Add to the list of tasks
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]  # Get selected task index
        tasks_listbox.delete(selected_index)  # Remove from Listbox
        tasks.pop(selected_index)  # Remove from list of tasks
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def update_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, new_task)  # Update Listbox
            tasks[selected_index] = new_task  # Update task list
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# UI Elements
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=12, command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=12, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=12, command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Run the application
root.mainloop()

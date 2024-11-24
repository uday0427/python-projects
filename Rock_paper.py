import tkinter as tk
from PIL import Image, ImageTk
import random

# Function to handle the game logic
def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    
    # Computer's choice is random
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Display the results
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("1920x1080")  # Full HD window

# Try loading and setting the background image
try:
    # Use the correct path to your image (change to your file path)
    background_image_path = r"C:\Users\ganig\Downloads\1_hPhzeFD3htF7ly1AMmAVbw.png"
    
    # Open and resize the image
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((1920, 1080))  # Resize to fit the window
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a canvas to hold the background image
    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)  # Make canvas fill the window
    
    # Add the background image to the canvas
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # Keep a reference to the image to prevent garbage collection
    canvas.image = background_photo

except Exception as e:
    print(f"Error loading image: {e}")

# Create a frame for buttons and other UI elements with a classy dark theme
frame = tk.Frame(root, bg="#2C3E50", bd=10, relief="solid", borderwidth=3)
frame.place(relwidth=1, relheight=1)  # Make the frame fill the window

# Game instructions label with modern font and classy color
instructions = tk.Label(frame, text="Choose Rock, Paper or Scissors", font=("Helvetica Neue", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
instructions.pack(pady=30)

# Button frame with rounded edges and modern look
button_frame = tk.Frame(frame, bg="#2C3E50")
button_frame.pack()

# Rock, Paper, and Scissors buttons with new colors and rounded edges
def create_button(text, color, command, row, column):
    button = tk.Button(button_frame, text=text, font=("Helvetica Neue", 16), bg=color, fg="white", width=12, height=2, bd=0, relief="flat", command=command)
    button.grid(row=row, column=column, padx=20, pady=20)
    return button

# Assign row and column indices to buttons
rock_button = create_button("Rock", "#2980B9", lambda: play_game('rock'), 0, 0)
paper_button = create_button("Paper", "#E67E22", lambda: play_game('paper'), 0, 1)
scissors_button = create_button("Scissors", "#16A085", lambda: play_game('scissors'), 0, 2)

# Creating a label to display the result of the game
result_label = tk.Label(frame, text="", font=("Helvetica Neue", 18), fg="#ECF0F1", bg="#2C3E50")
result_label.pack(pady=30)

# Running the application
root.mainloop()

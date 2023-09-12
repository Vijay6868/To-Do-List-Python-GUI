import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.geometry("400x200")

# Create a label
label = tk.Label(root, text="")
label.pack()

# Create a button without an initial command
button = tk.Button(root, text="Click Me")
button.pack()

# Define a new command to be associated with the button
def new_button_click():
    label.config(text="New Button Clicked!")

# Set the new command for the button using config()
button.config(command=new_button_click)

root.mainloop()

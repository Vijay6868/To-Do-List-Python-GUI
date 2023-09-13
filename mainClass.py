import datetime
import os
import tkinter as tk

os.system('clear')

from Task import Task

# creating object and testing all the methods
task1= Task(1,"Finish snap","Work on Joe Snap")
task1.taskNotes.append("this is my first note")
task1.outPutTask(task1)


# Graphical user interface code below:
# root = tk.Tk()

# root.geometry("800x500")
# root.title("TO DO LIST")
# lblTask = tk.Label(root,text="Tasks Created for Today", font=('Arial',18))
# lblTask.pack(padx=20,pady=20)

# txtbox = tk.Text(root,height=3, font=('Arial',16))
# txtbox.pack(padx=10)

# btnAddTask = tk.Button(root, text= "Add new task", font=('Arial',18))
# btnAddTask.pack()
# #newTask = tk.Tk()

# root.mainloop()


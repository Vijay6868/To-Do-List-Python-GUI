import datetime
import os
import tkinter as tk


from Task import Task

class AppGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("TO DO LIST")
        
        #self.root.configure(bg="gainsboro")
        self.sideMenu()
        #self.inputFrame()
        #self.menuFrame()

        self.root.mainloop()

     # configuring form   
    def menuFrame(self):
        frame= tk.Frame(self.root)
        frame.config(bg="light blue",width=650,height=600)
        frame.pack(fill=tk.BOTH, expand=True,)
        return frame
    
    # side menu bar with all the buttons
    def sideMenu(self):
       
        frSideMenu = tk.Frame(self.root,width=250, height=100)

        btHome = self.sideMenuBt(frSideMenu,"To Do")        
        btAddTask = self.sideMenuBt(frSideMenu,"Add New Task")
        btCompleted = self.sideMenuBt(frSideMenu,"Completed")
        btExit = self.sideMenuBt(frSideMenu,"Exit")
        frSideMenu.config(bg="gray10",pady=10, padx=20)

        
        frSideMenu.pack(side=tk.LEFT,fill=tk.Y)

        def btAddTask_click():
            self.inputFrame()
        btAddTask.config(command=btAddTask_click)

    # styling side menu bar buttons.
    def sideMenuBt(self,frame,textin):
        button = tk.Button(frame, text=textin, font=('Arial',14),bg="gray10",relief="flat",fg="white")
        button.pack(side=tk.TOP,fill= tk.X)
        return button

     # user input frame to enter a new task, sytling fields and labels.   
    def inputFrame(self):
        frame = self.menuFrame()
        lblDate = self.customLabel("Date :",frame)
        tbDate = self.customField(frame)
        lblName = self.customLabel("Title :",frame)
        tbName = self.customField(frame)
        lblDescription = self.customLabel("Description :",frame)
        tbDescription = tk.Text(frame, wrap = tk.WORD, font=('Arial', 14),height=5, width=20)
        btnAdd = tk.Button(frame,text="Add", font=('Arial',14))
        btnAdd.pack()

        lblDate.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tbDate.grid(row=0, column=1, padx=10, pady=10)
        lblName.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tbName.grid(row=1, column=1, padx=10, pady=10, )
        lblDescription.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tbDescription.grid(row=2,column=1, padx=10, pady=10)
        btnAdd.grid(row=3,column=1,padx=10,pady=10)
      # styling labels
    def customLabel(self, textin,frame):
        label = tk.Label(frame,text=textin, font=('Arial',14),bg="light blue")
        #label.pack(side=tk.LEFT, padx=10, pady=10)
        return label
    
    # styling methods
    def customField(self,frame):
        textbox = tk.Entry(frame, font=('Arial', 14))
        #textbox.pack(side = tk.LEFT, padx=10, pady=10)
       
        return textbox

app =AppGUI()
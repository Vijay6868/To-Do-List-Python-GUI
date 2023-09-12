import datetime

class Task:
    def __init__(self,taskid, name, description) :
        self.name = name
        self.description = description
        self.taskid = taskid
        self.taskDate = datetime.datetime.now()
        self.taskNotes=[] # to store Task class objects

    def userInput(self,taskid):
        self.name = input('Enter your task name : ')
        self.description= input('Enter your task description : ')
        self.taskid = taskid
        self.taskDate = datetime.datetime.now()

    def outPutTask(self,task1):
        print("\nTask id : "+str(task1.taskid))
        print("Task name : "+task1.name)
        print("Task Date : "+str(task1.taskDate))
        print("Task description : "+task1.description+"\n")
        print("Notes attached to this task:")
        for i in range(0,len(self.taskNotes)):
            print(self.taskNotes[i]+"\n")

    

    
        

        
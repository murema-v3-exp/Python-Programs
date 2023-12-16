import customtkinter as ctk
import tkinter as tk
import os.path 
import sqlite3
import datetime

# Setting the display colour
ctk.set_appearance_mode("dark")

# Setting the color of the widgets in the window
ctk.set_default_color_theme("green")

# Class of the app
class App(ctk.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Connect to the database
        self.connection = sqlite3.connect("toDoList.db")

        # create a cursor to execute SQL commands which acts as pointer to the database connection
        self.cursor = self.connection.cursor()

        # creates a new table if one doenst exist
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Tasks(TaskID INTEGER PRIMARY KEY AUTOINCREMENT,Date TEXT, Time TEXT , Task TEXT)')

        # Setting the title of the application
        self.title("To-do List")

        # Sets the dimensions of the window
        self.geometry("600x700")

        # A container for the heading and buttons 
        self.topFrame = ctk.CTkFrame(self)
        self.topFrame.pack(padx = 60, pady = 0,fill = ctk.X,expand=True)
       # self.topFrame.pack(side = ctk.TOP)

        # Label for heading
        self.headingLabel = ctk.CTkLabel(self.topFrame, text = "Daily List")
        self.headingLabel.pack(pady = 15)
        self.headingLabel.configure(font=ctk.CTkFont(size=25, weight='bold',slant='roman'), text_color=("blue","white"))

        # A button for creating a task
        self.newTaskButton = ctk.CTkButton(self.topFrame,text ="NEW ENTRY",command=self.newTask)
        self.newTaskButton.pack(padx = 3, pady = 5)

        # A button for adding a new task to the to-do list
        self.addTaskButton = ctk.CTkButton(self.topFrame,text="ADD TASK",command=self.addTask)
        self.addTaskButton.configure(state = "disabled")
        self.addTaskButton.pack(padx = 3,pady = 5)

        # A container for the tasks
        self.taskContainer = ctk.CTkScrollableFrame(self)
        self.taskContainer.pack(pady=5, padx=60,side = ctk.TOP, fill="both", expand=True)
        
        # The textbox that accepts a new task entry
        self.newTaskEntry = ctk.CTkTextbox(self.topFrame)
        self.newTaskEntry.configure(height = 50)

        # to load previous task entries from the Tasks database
        self.cursor.execute('SELECT Task FROM Tasks')
        self.tasks = self.cursor.fetchall()

    # function for fetching saved data from database    
    def fetchData(self):
            for task in self.tasks:
                outputContainer = ctk.CTkFrame(self.taskContainer, height = 45,fg_color =("#44524B","#44524B"))
                outputContainer.pack(padx =5 ,pady=5, fill="x")
                oldTasks = ctk.CTkTextbox(outputContainer,height =25,activate_scrollbars=True)
                oldTasks.insert("0.0",task[0].strip())
                oldTasks.pack(padx = 8,pady =10,fill = "x")
                
                # button for removing the task
                btnRemoveTask = ctk.CTkButton(outputContainer,text = "DONE",command=lambda: self.removeTask(task[0]))
                btnRemoveTask.pack(padx=3,pady=5)
                oldTasks.configure(state = "disabled")

    # Method for creating a task
    def newTask(self):
        # An entry for a new task
        self.newTaskEntry.pack(padx = 5,pady = 5,fill = "x")

        self.addTaskButton.configure(state = "normal")
        #self.removeTaskButton.configure(state="normal")
        
        return self.newTaskEntry.get("0.0","end")  
    
    # Method for adding a new task to the to do list
    def addTask(self):

        # Panel that will contain the task text and a button for removing it
        outputContainer = ctk.CTkFrame(self.taskContainer, height = 35,fg_color =("#44524B","#44524B"))
        outputContainer.pack(padx =5 ,pady=5, fill="x")

        taskString = self.newTask()
        taskOutput = ctk.CTkTextbox(outputContainer,height = 25, activate_scrollbars=False)
        taskOutput.insert("0.0",taskString)
        taskOutput.configure(state="disabled")
        taskOutput.pack(padx = 8,pady = 10,fill = "x")
        taskOutput.configure(state="disabled")

        # button for removing the task
        btnRemoveTask = ctk.CTkButton(outputContainer,text = "REMOVE",command=lambda: self.removeTask(taskString))
        btnRemoveTask.pack(padx=3,pady=5)

        # adding the task to the database 
        day = datetime.datetime.now().strftime("%x")
        clock = datetime.datetime.now().strftime("%X")
        taskstoInsert = (day,clock,taskString)

        self.cursor.execute('INSERT INTO Tasks(Date, Time, Task) VALUES (?,?,?)',taskstoInsert)
        self.connection.commit()

        # deletes the Entry after a task is added
        self.newTaskEntry.delete("0.0","end")
        self.newTaskEntry.pack_forget() 
        self.addTaskButton.configure(state="disabled")

    def removeTask(self,toRemove):
        theID = (toRemove,) 
        self.cursor.execute('DELETE FROM Tasks WHERE Task = ?',theID)
        self.connection.commit()
        self.reset_program()

    def reset_program(self):
        self.destroy()
        main()
         
def main():
    app = App()
    app.fetchData()
    app.mainloop()

if __name__ == "__main__":
    main()
   



    
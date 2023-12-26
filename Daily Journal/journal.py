import customtkinter as ctk
import tkinter as tk
import os.path 
import sqlite3
import datetime


# Setting the display colour
ctk.set_appearance_mode("dark")

# Setting the color of the widgets in the window
ctk.set_default_color_theme("blue")

# Class of the app
class App(ctk.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Connect to the database
        self.connection = sqlite3.connect("DailyJournal.db")

        # create a cursor to execute SQL commands which acts as pointer to the database connection
        self.cursor = self.connection.cursor()

        # creates/loads a new table for journal entries
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Entries(Title Text, Date TEXT, Mood TEXT , Entry TEXT)')

        # Setting the title of the application
        self.title("Daily Reflections")

        # Sets the dimensions of the window
        self.geometry("600x700")

        self.title = ctk.CTkLabel(self,text="Everyday Reflections")
        self.title.configure(font=ctk.CTkFont(size=35, weight='bold',slant='roman'), text_color=("black","white"))
        self.title.pack(pady=5)

        self.btnNewEntry = ctk.CTkButton(self,text="New Journal Entry",command =self.new_journal_entry)
        self.btnNewEntry.pack(pady=10)

        self.btnLoadEntries = ctk.CTkButton(self,text="View Entries",command=self.show_entries)
        self.btnLoadEntries.pack(pady=10)

        self.textFrame =ctk.CTkFrame(self)
        self.textbox = ctk.CTkTextbox(self.textFrame,width=500, height=400, corner_radius= 5)
        self.entryTitle = ctk.CTkEntry(self.textFrame,placeholder_text="Title")

        self.moods = ["Contempt","Exhilaration","Melancholy","Determination","Exhausted","Annoyed",'Neutral']
        

    def new_journal_entry(self):
        self.textFrame.pack(padx = 20, pady = 0,side="top",expand=True)
      
        
        dateCreated = datetime.datetime.now().strftime("%x")

        dateLabel = ctk.CTkLabel(self.textFrame,text=dateCreated)
        dateLabel.grid(row=0,column=0,padx=10,pady=10)

        self.entryTitle.grid(row=0,column=1,padx=10,pady=10)

        dateLabel.configure(font=ctk.CTkFont(size=18, weight='normal',slant='roman'), text_color=("black","white"))

        btnSaveEntry = ctk.CTkButton(self.textFrame,text = "Save", command=self.save)
        btnSaveEntry.grid(row = 2,column=2,pady=10)

        self.textbox.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
        self.textbox.configure(font=("Times New Roman",16))
        self.textbox.configure(text_color=("#13262F","#BCD2EE"))

        self.moodTracker = ctk.CTkOptionMenu(self.textFrame,values=self.moods)
        self.moodTracker.grid(row=0,column=2,padx=10,pady=10)

        

    def save(self):
        title = self.entryTitle.get()
        entry = self.textbox.get("0.0","end")
        dateCreated = datetime.datetime.now().strftime("%x")
        mood = self.moodTracker.get()
        toInsert = (title,dateCreated,mood,entry)

        self.cursor.execute("INSERT INTO Entries(Title,Date,Mood,Entry) VALUES(?,?,?,?)",toInsert)
        self.connection.commit()

    def show_entries(self):
        self.textFrame.pack(padx = 20, pady = 0,side="TOP",expand=True)

app = App()
app.mainloop()


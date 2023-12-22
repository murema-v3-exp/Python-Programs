
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import os.path
#from PIL import Image, ImageTk
#from playsound import playsound
import time

class Pomodoro(tk.Tk):
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting the title of the application
        self.title("Pomodoro Timer")

        # Setting the dimentsions of the window
        self.geometry("300x300")
        self.resizable(False,False)
  
        # Adding a background image
    
        self.my_image = tk.PhotoImage(file="images/Lhourglass.png")

        self.canvas = tk.Canvas(self,width = 300,height= 300)
        self.canvas.pack(fill="both",expand= True)
        # Set image in canvas
        self.canvas.create_image(0,0,image=self.my_image, anchor="nw")
         
        # Initializing variables
        self.time_remaining = 25 * 60
        self.strTime = tk.StringVar(self)
        self.time_stopped = False
        self.onBreak = False
        
        # The label that will display the time
        self.timer_label = tk.Label(self,text = "25:00", font=("Helvetica",16))
        self.label_win = self.canvas.create_window(150,60,anchor="center",window=self.timer_label)
        self.timer_label.configure(bg="#0e101c",fg="#f7f296")
     
        # The start button
        self.button_start = tk.Button(self, text = "START",command=lambda: self.timer_start(25*60))
        self.button_start.configure(bg="#0e101c",fg="#f7f296")
        self.buttonStartWin = self.canvas.create_window(10,10,anchor="nw",window=self.button_start)

        # The stop button
        self.button_stop = tk.Button(self, text = "STOP",command=self.stop)
        self.buttonStopWin = self.canvas.create_window(255,10,anchor="nw",window=self.button_stop)
        self.button_stop.configure(bg="#0e101c",fg="#f7f296")

   def timer_start(self,timer):
        # Activating the pause button
        self.button_stop.config(state="normal")
        self.timer_label.config(textvariable=self.strTime)
    
     
        while timer >= 0 and not self.time_stopped:  
            if timer == 0:
               if self.onBreak:
                   messagebox.showinfo("Pomodo Timer: Break is over","YOUR BREAK IS OVER MY DEAR, GET BACK TO WORK")
               messagebox.showinfo("Pomodoro Timer: Break has just started ","TAKE A BREAK, DO SOME PUSH UPS, DRINK WATER")
               self.break_()
               self.onBreak = False
               
            mins, secs = divmod(timer,60)
            self.strTime.set('{:02d}:{:02d}'.format(mins, secs))
            self.update()
            time.sleep(1)
            timer -= 1
    
   def stop(self):
        # Stops and resets the timer
        self.strTime.set("25:00")
        self.time_stopped = True

   def break_(self):   
       self.timer_start(5*60)
       self.onBreak = True      

app = Pomodoro()
app.mainloop()


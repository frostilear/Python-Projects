import time
import tkinter as tk
class Clock(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Clock")
        self.canvas= tk.Canvas(self,height=600,width=600,background="#0F1300")
        self.canvas.grid(row=0,column=0)
        self.geometry("%dx%d+%d+%d"%(600,600,self.winfo_screenwidth()/2-300,self.winfo_screenheight()/2-300))
        self.Time()
    def Time(self):
        secs=time.localtime()[5]
        if secs==0:
            self.canvas.delete("arc")
        mins=time.localtime()[4]
        hrs=time.localtime()[3]
        self.canvas.create_arc(150,150,450,450,start=90,extent=(-secs*6),outline="#B4F8C8",style="arc",width=10,tag="arc")
        self.canvas.create_arc(172,172,428,428,start=90,extent=(-mins*6),outline="#07D2BE",style="arc",width=25,tag="arc")
        self.canvas.create_arc(210,210,390,390,start=90,extent=(-hrs*30),outline="#F24E70",style="arc",width=40,tag="arc")
        self.after(1,self.Time)
if __name__ == "__main__":
    Clock().mainloop()
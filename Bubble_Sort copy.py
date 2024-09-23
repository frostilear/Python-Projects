import tkinter as tk
from tkinter import ttk
import random
import time
class Bubble(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Bubble Sort")
        self.height,self.width=600,1000
        self.canvas=tk.Canvas(self,height = self.height,width = self.width,background="black");self.canvas.grid(row=0,column=0)
        self.values=[]
        self.check=0
        self.pixel=0
        self.but=ttk.Button(self,text="Sort!",command=self.buttonfun)
        self.but.grid(row=0,column=1)
        self.CreateLines()
    def CreateLines(self):
        self.canvas.delete("line")
        for pixel in range(self.width):
            heights = random.randrange(0,(self.height+1))
            self.values.append(heights)
            self.canvas.create_line(pixel,self.height,pixel,self.values[pixel],fill='white',tags="line{}".format(pixel))
        if self.check==0:
            self.n=len(self.values)
            self.Sort()

    def Sort(self):
        for i in range(self.n):
            for j in range(0,self.n-i-1):
                if (self.values[j]) < (self.values[j+1]):
                    self.values[j],self.values[j+1]= self.values[j+1],self.values[j]
                    #self.check=1
                    #self.after(1,self.CreateLines)
    def buttonfun(self):
        self.canvas.delete("line{}".format(self.pixel))
        self.canvas.create_line(self.pixel,self.height,self.pixel,self.values[self.pixel],fill="white")
        self.pixel+=1
        self.after(1,self.buttonfun)

Bubble().mainloop()
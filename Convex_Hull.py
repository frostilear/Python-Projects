from numpy import array,cross,subtract
import tkinter as tk
from tkinter import ttk
import random
class Convex(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Convex Hull Algorithm")
        self.canvas=tk.Canvas(self,height=600,width=600,background="black")
        self.canvas.grid(row=0,column=0)
        self.size=5
        self.index=0
        self.minpoint=array([601,0])
        self.points=[]
        self.var=0
        self.nextindex=-1
        bt=ttk.Button(self,text="Start",command=self.Draw)
        bt.grid(row=0,column=1)
        i=0
        while i<100:
            self.CreatePoints(array([random.randrange(10,591),random.randrange(10,591)]))
            i+=1
    def CreatePoints(self,pointArray):
        self.x1=(pointArray[0]-self.size)
        self.y1=(pointArray[1]-self.size)
        self.x2=(pointArray[0]+self.size)
        self.y2=(pointArray[1]+self.size)
        self.canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill="white",outline="white")
        self.points.append(pointArray)
        self.nextvertex=self.points[0]
        self.currentpoint=self.minpoint
        if pointArray[0]<self.minpoint[0]:
            self.minpoint=pointArray
            self.canvas.delete("minpoint")
            self.canvas.create_oval((self.minpoint[0]-self.size),self.y1,(self.minpoint[0]+self.size),self.y2,fill="lime",tag="minpoint",outline="lime")
        else:
            pass
    def Draw(self):
        self.var+=1
        if 100>=self.var:
            self.canvas.delete("check")
            self.checking=self.points[self.index]
            cross=self.CrossProduct(self.nextvertex,self.currentpoint,self.checking)
            if cross<0:
                self.canvas.delete("next")
                self.nextvertex=self.checking
                self.nextindex=self.index
            self.canvas.create_line(self.currentpoint[0],self.currentpoint[1],self.checking[0],self.checking[1],fill="white",tag="check")
            self.canvas.create_line(self.currentpoint[0],self.currentpoint[1],self.nextvertex[0],self.nextvertex[1], fill="lime",tag="next",width=3)
            self.index+=1
            self.after(1,self.Draw)
            if self.index==100:
                self.var=0
                if (self.nextvertex==self.minpoint).all():
                    self.canvas.delete("next","check")
                    self.var=101
                self.canvas.create_line(self.currentpoint[0],self.currentpoint[1],self.nextvertex[0],self.nextvertex[1], fill="blue",width=5)
                self.currentpoint=self.nextvertex
                self.canvas.create_oval(self.currentpoint[0]-(self.size+5),self.currentpoint[1]-(self.size+5),self.currentpoint[0]+(self.size+5),self.currentpoint[1]+(self.size+5),fill="blue",outline="blue")
                self.index=0
                self.nextvertex=self.minpoint
    def CrossProduct(self,nextvertex,currentpoint,checking):
        a=subtract(nextvertex,currentpoint)
        b=subtract(checking,currentpoint)
        crosses=cross(a,b)
        return crosses
Convex().mainloop()
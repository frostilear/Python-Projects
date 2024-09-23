from math import sin,cos,pi
import tkinter as tk
from tkinter import ttk
import random
l1,l2,=85,85
g=9.81
class DoublePendulum(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Double Pendulum")
        self.canvas=tk.Canvas(self,width=600,height=600,background="#343434")
        self.canvas.grid(row=0,column=0)

        self.rand=random.randrange(0,361)
        self.rand2=random.randrange(0,361)

        self.a1_v=0
        self.a2_v=0
        self.a1=self.rand
        self.a2=self.rand2
        self.m1=5
        self.m2=5

        self.speed=0.1
        self.somevar=[]
        x1=l1*sin(self.a1)
        y1=-l1*cos(self.a1)

        x2=x1+l2*sin(self.a2)
        y2=y1-l2*cos(self.a2)
        self.slider1=tk.Scale(self,orient="horizontal",from_=1,to=50,command=self.slidercommand,label="Mass Of Bob 1")
        self.slider2=tk.Scale(self,orient="horizontal",from_=1,to=50,command=self.slidercommand,label="Mass Of Bob 2")
        self.a1slider=tk.Scale(self,orient="horizontal",from_=1,to=360,command=self.slidercommand,label="Angle 1")
        self.a2slider=tk.Scale(self,orient="horizontal",from_=1,to=360,command=self.slidercommand,label="Angle 2")
        self.a1slider.grid(row=3,column=1)
        self.a2slider.grid(row=4,column=1)
        self.slider1.grid(row=1,column=1)
        self.slider2.grid(row=2,column=1)
        but=tk.ttk.Button(self,text="Click To Simulate!")
        but.grid(row="0",column="1")
        but.config(command=self.something)
        self.size=2
        self.size2=2
        self.canvas.create_line(300,250,300+x1,250+(-y1),width=5,fill="#CCCCCC",tags="pendulum")
        self.geometry("%dx%d+%d+%d"%(800,850,self.winfo_screenwidth()/2-400,self.winfo_screenheight()/2-425))

        self.canvas.create_line(300+x1,250+(-y1),300+x2,250+(-y2),width=5,fill="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size)+x1,(240-self.size)+(-y1),(305+self.size)+x1,(260+self.size)+(-y1),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size2)+x2,(240-self.size2)+(-y2),(305+self.size2)+x2,(260+self.size2)+(-y2),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")
    def slidercommand(self,idk):
        self.canvas.delete("pendulum")
        self.a1=self.rand+self.a1slider.get()*2*0.01
        self.a2=self.rand2+self.a2slider.get()*2*0.01
        self.m1=self.slider1.get()
        self.m2=self.slider2.get()
        self.size=self.m1/2
        self.size2=self.m2/2
        x1=l1*sin(self.a1)
        y1=-l1*cos(self.a1)

        x2=x1+l2*sin(self.a2)
        y2=y1-l2*cos(self.a2)
        
        self.canvas.create_line(300,250,300+x1,250+(-y1),width=5,fill="#CCCCCC",tags="pendulum")


        self.canvas.create_line(300+x1,250+(-y1),300+x2,250+(-y2),width=5,fill="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size)+x1,(240-self.size)+(-y1),(305+self.size)+x1,(260+self.size)+(-y1),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size2)+x2,(240-self.size2)+(-y2),(305+self.size2)+x2,(260+self.size2)+(-y2),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")

    def something(self):
        self.geometry("%dx%d"%(600,600,))
        self.Calculate()
    def Calculate(self):
        self.canvas.delete("trace")
        self.canvas.delete("pendulum")    
        #all the math is from https://www.myphysicslab.com/pendulum/double-pendulum-en.html
        num1=(-g*(2*self.m1+self.m2)*sin(self.a1))
        num2=-self.m2*g*sin(self.a1-2*self.a2)
        num3 = (
        -2
        * sin(self.a1 - self.a2)
        * self.m2
        * (self.a2_v ** 2 * l2 + self.a1_v ** 2 * l1 * cos(self.a1 - self.a2))
    )
        deno1=l1*(2*self.m1+self.m2-self.m2*cos(2*self.a1-2*self.a2))

        self.a1_a=(num1+num2+num3)/deno1

        num4 = 2*sin(self.a1-self.a2)
        num5=(self.a1_v**2*l1*(self.m1+self.m2))
        num6=g*(self.m1+self.m2)*cos(self.a1)
        num7=self.a2_v**2*l2*self.m2*cos(self.a1-self.a2)
        deno2=l2*(2*self.m1+self.m2-self.m2*cos(2*self.a1-2*self.a2))

        self.a2_a=(num4*(num5+num6+num7))/deno2


        self.a1_v+=self.a1_a*self.speed
        self.a2_v+=self.a2_a*self.speed
        self.a1+=self.a1_v*self.speed
        self.a2+=self.a2_v*self.speed

        x1=l1*sin(self.a1)
        y1=-l1*cos(self.a1)

        x2=x1+l2*sin(self.a2)
        y2=y1-l2*cos(self.a2)

        self.somevar.append((300+x2,250+(-y2),300+x2,250+(-y2)))

        self.canvas.create_line(self.somevar,fill="#DA5959",tags="trace",width=2)

        self.canvas.create_line(300,250,300+x1,250+(-y1),width=5,fill="#CCCCCC",tags="pendulum")


        self.canvas.create_line(300+x1,250+(-y1),300+x2,250+(-y2),width=5,fill="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size)+x1,(240-self.size)+(-y1),(305+self.size)+x1,(260+self.size)+(-y1),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")

        self.canvas.create_oval((285-self.size2)+x2,(240-self.size2)+(-y2),(305+self.size2)+x2,(260+self.size2)+(-y2),fill="#CCCCCC",outline="#CCCCCC",tags="pendulum")
        
        self.after(1,self.Calculate)
        
DoublePendulum().mainloop()
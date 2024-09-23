from math import pi
import tkinter as tk
r=input("Radius of the circle?")
area=pi*float(r)**2
print("The area is: ",area)
if float(r)<21.1:
    print("The circle looks like:")
    Window=tk.Tk()
    canvas=tk.Canvas(Window,height=800,width=800,background="#343434")
    canvas.grid(row=0,column=0)
    cm=400.0
    canvas.create_oval(cm-(float(r)*37.7952755906),cm-(float(r)*37.7952755906),cm+(float(r)*37.7952755906),cm+(float(r)*37.7952755906),fill="white",outline="white")
    Window.mainloop()
else:
    print("The Radius is too big to be represented visually.")
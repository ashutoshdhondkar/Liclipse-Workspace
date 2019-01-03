# program to demonstrate spinbox in python
from tkinter import *

class SpinBox:
    def __init__(self,root):
        self.f=Frame(root,height=350,width=350)
        self.f.propagate(0)
        self.f.pack()
        
        # let's create control variable for spinbox
        self.val1=IntVar()
        self.val2=StringVar()
        
        # create a spinbox with numbers 5-15
        self.s1=Spinbox(self.f,from_=5,to=15,textvariable=self.val1,width=15,fg="blue",bg="yellow")

        
        # create a spinbox with strings
        self.s2=Spinbox(self.f,values=('ashutosh','Nayan','Neha'),textvariable=self.val2)
        
        #lets create  button and bind it with display()
        self.butt=Button(self.f,text="click me",command=self.display)
        
        #place spinbox and buttons
        
        self.s1.place(x=50,y=50)
        self.s2.place(x=50,y=100)
        self.butt.place(x=50,y=150)
        
    def display(self):
        
        a=self.val1.get()
        b=self.val2.get()
        
        print(a)
        print(b)
        
        
root=Tk()
gui=SpinBox(root)
root.mainloop()
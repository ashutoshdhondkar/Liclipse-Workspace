# program to demonstrate listbox
from tkinter import *

class LB:
    def __init__(self,root):
        self.lst=['ashutosh','nayan','dhondkar']
        self.lb=Listbox(root,selectmode=SINGLE)
        
        for i in self.lst:
            self.lb.insert(END,i)
            
        self.lb.pack()
        
        #let's create a textbox
        
        
root=Tk()
gui=LB(root)
root.mainloop()
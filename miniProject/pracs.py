from tkinter import *
import MySQLdb

class GUI:
    def __init__(self,root):
        self.f=Frame(root,height=800,width=800,bg="yellow")
        self.f.propagate(0)
        self.f.pack()
        root.title("Exam Form")
        self.mainLabel=Label(self.f,text="Exam Form",bg="yellow",font=('Times',30,'bold italic underline'))
        self.mainLabel.pack()
        self.labelName=Label(self.f,text="Full NAme : ",bg="yellow",font=('Times',15,'bold'))
        self.labelName.place(x=100,y=100)
        self.nameEntry=Entry(self.f,width=60)
        self.nameEntry.place(x=250,y=105)
        self.labelPrn=Label(self.f,text="PRN :",bg="yellow",font=('Times',15,'bold'))
        self.labelPrn.place(x=100,y=150)
        self.prnEntry=Entry(self.f,width=30)
        self.prnEntry.place(x=250,y=155)
        self.sem=IntVar()
        self.labelsem=Label(self.f,text="SEM :",bg="yellow",font=('Times',15,'bold'))
        self.labelsem.place(x=500,y=50)
        self.semEntry=Spinbox(self.f,from_=1,to=8,textvariable=self.sem)
        self.semEntry.place(x=600,y=55)
        self.branch=StringVar()
        self.labelBranch=Label(self.f,text="Branch : ",bg="yellow",font=('Times',15,'bold'))
        self.labelBranch.place(x=100,y=200)
        self.branchEntry=Spinbox(self.f,value=('CE','ME','IT','EXTC','PPT'),textvariable=self.branch)
        self.branchEntry.place(x=250,y=205)
        self.labelMobile=Label(self.f,text="Mobile No.",bg="yellow",font=('Times',15,'bold'))
        self.labelMobile.place(x=100,y=250)
        self.MobileEntry=Entry(self.f,width=30)
        self.MobileEntry.place(x=250,y=255)
        
        #self.bt1=Checkbutton(self.f,text="Foo",bg="yellow",activebackground="yellow")
        #self.bt1.pack()
        
        self.sublabel=Label(self.f,text="Subjects",bg="yellow",font=('Times',15,'bold italic underline'))
        self.sublabel.place(x=50,y=300)   
        #self.pracsLabel=Label(self.)     
root=Tk()
gui=GUI(root)
root.mainloop()
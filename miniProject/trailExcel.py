import pandas as pd
from tkinter import *

root=Tk()

frame=Frame(root,height=700,width=1000,bg="orange").pack()

file_path="C:\\Users\\Admin\\My Documents\\LiClipse Workspace\\miniProject\\Book1.xlsx"

x1=pd.ExcelFile(file_path)
df=x1.parse('Sheet1')


m=Message(frame,text=df ,bg="orange",width=800,font=('Times',15,'bold '))


m.place(x=100,y=100)

root.mainloop()

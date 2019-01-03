from tkinter import *
from tkinter import filedialog
# filedialog is a separate module in tkinter so we need to import it separately

class MenuBAR:
    def __init__(self,root):
        # let's create a menubar
        self.menubar=Menu(root)
        
        #lets config it inside the root
        root.config(menu=self.menubar)
        
        #let's create a "File" menu
        #file_menu be the object
        self.file_menu=Menu(root,tearoff=0)
        
        #let's add items to file_menu i.e. add menus to "File"
        self.file_menu.add_command(label="Open",command=self.file_open)
        self.file_menu.add_command(label="Save",command=self.file_save)
        
        # let's add a separator
        #separator is nothing but a dotted line(----)
        self.file_menu.add_separator()
        
        # lets create an option to exit
        self.file_menu.add_command(label="Exit",command=root.destroy)
        
        #let's place our file_menu object into menubar with label as "File"
        self.menubar.add_cascade(label="File",menu=self.file_menu)
        
    def file_open(self):
        # open a file dialog box and accept file name
        self.filename=filedialog.askopenfilename(parent=root,title="select a file",filetype=(("Text files","*.txt"),("Excel files","*.xlsx"),("All files","*.*")))
        
        if(self.filename != None):
            # open the file in read mode
            f=open(self.filename,'r')
            # read the contents of file
            contents=f.read()
            
            #create a textbox and add it to root window
            self.t=Text(root,width=80,height=20,wrap=WORD)
            self.t.pack()
            
            self.t.insert(1.0,contents)
            f.close()
    
    
    def file_save(self):
        # open a dialog box and type a file name
        self.filename=filedialog.asksaveasfilename(parent=root,defaultextension=".txt")
        # if cancel button is not clicked in dialog box
        if(self.filename!=None):
            f=open(self.filename,'a')
            # get the contents of text box
            contents=str(self.t.get(1.0,END))
            #store the contents into file
            f.write(contents)
            f.close()
             
        
        
root=Tk()
root.geometry("400x400")
obj=MenuBAR(root)
root.mainloop()

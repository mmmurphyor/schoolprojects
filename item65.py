#Margret Murphy item 61(64 now)
#python
#12/13/16

from tkinter import *
from tkinter import ttk
from tkinter import  filedialog
import os, shutil, sys, datetime, time


class XferApp:

        def __init__(self, parent):
            self.app_parent = parent
            self.xfer_app = Frame(parent)
            self.xfer_app.grid()
        
            self.title_label = Label(self.xfer_app, text = 'Transfer New or Changed Files')
            self.title_label.grid(column = 0, row = 1, columnspan = 2)

            self.source_var = StringVar()
            self.source_label = Label(self.xfer_app, textvariable = self.source_var)                        
            self.source_label.grid(column = 0, row = 2, columnspan = 2, sticky = 'W')
            
            self.button_source = Button(self.xfer_app, command = lambda: self.get_directory(), text = 'Select Source Directory')
            self.button_source.grid(column = 3, row = 2, sticky = 'E')
            
            self.dest_var = StringVar()
            self.dest_label = Label(self.xfer_app, textvariable = self.dest_var)
            self.dest_label.grid(column = 0, row = 6, columnspan = 2, sticky = 'W')

            self.button_dest = Button(self.xfer_app, command = lambda: self.dest_directory(), text = 'Select Destination Directory')
            self.button_dest.grid(column = 3, row = 6, sticky = 'E')

            self.update_var = StringVar()
            self.button_update = Button(self.xfer_app, command = lambda:self.move_files(), text = 'Move Files')
            self.button_update.grid(column = 3, row = 8, sticky = 'E')
            self.update_label = Label(self.xfer_app, "")
            self.update_label.grid(column = 0, row = 8, sticky = 'W')
            
        def get_directory(self):
            dir_name = filedialog.askdirectory(parent = self.xfer_app,initialdir="C:/",)
            self.source_var.set(dir_name)
            self.source_label = dir_name           
            
        def dest_directory(self):
            dest_dir_name = filedialog.askdirectory(parent = self.xfer_app, initialdir = "C:/",)
            self.dest_var.set(dest_dir_name)
            self.dest_label = dest_dir_name

        def move_files(self):
            self.source_path = self.source_var.get()
            self.dest_path = self.dest_var.get()

            with open('output.txt', 'w') as output_file:      
                for file in os.listdir(self.source_path):
                    src_file = os.path.join(self.source_path, file)
                    dest_file = os.path.join(self.dest_path, file)
                    counter = 0
                    mtime = os.stat(src_file).st_mtime  #gets the timestamp
                    t2 = datetime.datetime.fromtimestamp(mtime)   #converts to a datetime object
                    timenow = datetime.datetime.now() #gets current time
                    modifyhour = t2.strftime('%H:%M:%S') #formats the two times
                    nowtime = timenow.strftime('%H:%M:%S')
                    difference = timenow-t2 #compares the times
                    if difference.days <1: #checks to see if file is newer than a day.
                        shutil.move(src_file, dest_file)
                        output_file.write((str(dest_file)) + os.linesep)
                        
                    
                                    
            
                      
root = Tk()
xfer_app = XferApp(root)
root.mainloop()

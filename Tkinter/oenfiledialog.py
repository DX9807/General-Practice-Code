# -*- coding: utf-8 -*-
from tkinter import * 
from tkinter.filedialog import * 
from tkinter.scrolledtext import ScrolledText
root = Tk() 
textbox = ScrolledText() 
textbox.grid()
filename=askopenfilename(initialdir='c:\\python31\\', filetypes=[('Text files', '.txt'),
('All files', '*')])
s = open(filename).read() 
textbox.insert(1.0, s)
mainloop()


# -*- coding: utf-8 -*-
import tkinter as tk

def calculate():
    temp=int(entry.get())
    temp=9/5*temp+32
    output_label.configure(text='Coverted::{:1f}'.format(temp))
    
    entry.delete(0,END)
    
    
root=tk.Tk()
root.title("Converter")
message_label=tk.Label(text="Enter a temprature:")

output_label=tk.Label()
entry=tk.Entry(width=4)
calc_button=tk.Button(text="Ok",command=calculate)

message_label.grid(row=0,column=0)
entry.grid(row=0,column=1)
calc_button.grid(row=0,column=2)
output_label.grid(row=1,column=0,columnspan=3)
tk.mainloop()

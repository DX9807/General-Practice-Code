import tkinter as tk

def show():
    e1=entry1.get()
    e2=entry2.get()
    #print("You entered ::")
    output_label.configure(text=e1+e2)

root=tk.Tk()
root.title('Gui1')
label1=tk.Label(root,text='FirstName')
label1.pack(side='left')
entry1=tk.Entry(root)
entry1.pack(side='left')
label2=tk.Label(root,text='LastName')
label2.pack(side='left')
entry2=tk.Entry(root)
entry2.pack(side='left',expand='YES')
tk.Label(text='You have entered::').pack(side="bottom")


output_label=tk.Label()

output_label.pack(side='left')
button=tk.Button(text='Ok',command=show)
button.pack()

root.mainloop()

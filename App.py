from tkinter import *
from tkinter import ttk
import importlib
import time
a = ("Model_Selection")

root = Tk()
root.geometry("500x150+400+300")
root.overrideredirect(True)
v = 0
c = ttk.Progressbar(root, orient=HORIZONTAL,length=500,maximum=150, mode='determinate')

root.update_idletasks()

c.pack(ipady=20)
for x in range(150):
    c['value'] += 1
    root.update_idletasks()
    time.sleep(0.02)
    v += 1
    if v == 150:
        root.destroy()
        importlib.import_module(a)

root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('simple progress bar')
root.geometry('400x300')

label = tk.Label(root,text = 'downloading....',font = ('arial', 15))
label.pack(pady=20)

progress1 = ttk.Progressbar(root,orient='horizontal',length=300,mode='determinate')
progress1.pack(pady=20)

progress2 = ttk.Progressbar(root,orient='horizontal',length=300,mode='determinate')
progress2.pack(pady=50)

def start_progress1(i=0):
    if i <= 100:
        progress1['value'] = i
        root.after(30, start_progress1, i+1)

def start_progress2(i=0):
    if i <= 100:
        progress2['value'] = i
        root.after(50, start_progress2, i+1)

btn1 = tk.Button(root, text='Start Progress 1', command=start_progress1)
btn1.pack(pady=5)
btn2 = tk.Button(root, text='Start Progress 2', command=start_progress2)
btn2.pack(pady=5)
root.mainloop()
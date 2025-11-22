import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("please enter a task")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning('warning',"please select something")

def clear_task():
    listbox.delete(0,tk.END)

root = tk.Tk()
root.title("TaskManager")
root.geometry('400x500')

entry=tk.Entry(root,width=25)
entry.pack(pady=10)

btn1 = tk.Button(root, text='Add Task', command=add_task)
btn1.pack(pady=5)

listbox=tk.Listbox(root,width=30,height=20)
listbox.pack(pady=10)

btn2 = tk.Button(root, text='Delete Task', command=delete_task)
btn2.pack(pady=5)

btn2 = tk.Button(root, text='Clear Task', command=clear_task)
btn2.pack(pady=5)

root.mainloop()

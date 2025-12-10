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
root.title("TaskBar")
root.geometry('500x400')
root.config(bg = 'black')

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff = 0)

def new_file():
    new_window = tk.Toplevel(root)
    new_window.title('new file')
    new_window.geometry('200x100')
    tk.Label(new_window, text = 'this is the new window').pack(pady=20)

entry=tk.Entry(root,width=25)
entry.pack(pady=10)

btn1 = tk.Button(root, text='Add Task', command=add_task, fg='red', bg='white')
btn1.pack(pady=5)

listbox=tk.Listbox(root,width=50,height=40)
listbox.pack(pady=10)

btn2 = tk.Button(root, text='Delete Task', command=delete_task, fg='purple', bg='white')
btn2.pack(pady=10)

btn3 = tk.Button(root, text ='Clear Task', command=clear_task, fg='blue', bg='white')
btn3.pack(pady=15)

root.mainloop()
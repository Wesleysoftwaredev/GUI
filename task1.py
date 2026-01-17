import tkinter as tk

from tkinter import messagebox
root = tk.Tk()
root.title("GUI Message box")
root.geometry('300x200')

def show_message():
    messagebox.showinfo("message", "Hi, I am Wesley.")

def clear_message():
    messagebox.showinfo("message", "")

button1 = tk.Button(root, text="Button 1", command=show_message)
button1.pack(pady=5)

button2 = tk.Button(root, text="Button 2", command=clear_message)
button2.pack(pady=5)

root.mainloop()
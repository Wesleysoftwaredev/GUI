import tkinter as tk
from tkinter import ttk

count = 0

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

def increase():
    global count
    count +=1
    label.config(text=str(count))

root = tk.Tk()
root.title("Counter App")
root.geometry("200x120")

label = ttk.Label(root, text="0", font=("Arial", 20))
label.pack(pady=10)

button = ttk.Button(root, text="decrease", command=decrease)
button.pack()

button = ttk.Button(root, text="increase", command=increase)
button.pack()

root.mainloop()
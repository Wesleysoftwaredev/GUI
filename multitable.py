import tkinter as tk
from tkinter import ttk,messagebox

def show_table():

    try:
        n = int(num_var.get())

    except ValueError:
        messagebox.showerror("invalid input","Please enter an integer")
        return
    
    try:
        start = int(start_var.get())
        end = int(end_var.get())
    except ValueError:
        messagebox.showerror("Invalid input","Please enter integers for start and end")
        return
    
    if start>end:
        messagebox.showerror("Invalid range", "Start must be les or equal to End")
        return
    
    lines = []
    for i in range(start,end+1):
        lines.append(f"{n} x {i}= {n*i}")
    output_text = "\n".join(lines)
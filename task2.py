import tkinter as tk

from tkinter import messagebox
root=tk.Tk()
root.title("User Greeting")
root.geometry("350x200")

bg_color = "lightblue"
root.configure(bg=bg_color)

instruction = tk.Label(root)
instruction.pack(pady=5)

name_entry = tk.Entry(root)
name_entry.insert(0, "Name: ")
name_entry.pack(pady=5)

greeting_label = tk.Label(root, text="", font=("Arial", 12))
greeting_label.pack(pady=10)

def show_greeting():
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name} how are you doing.")

def clear_greeting():
    greeting_label.config(text="")
    name_entry.delete(0, tk.END)

greet_button = tk.Button(root, text="Greet", command = show_greeting)
greet_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command = clear_greeting)
clear_button.pack(pady=5)

root.mainloop()
    
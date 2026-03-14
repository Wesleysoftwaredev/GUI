import tkinter as tk
from tkinter import ttk
import random

def generate():
    label.config(text=str(random.randint(1, 100)))

root = tk. Tk()

label = ttk.Label(root, text="0", font=("Arial", 20))
label.pack(pady=10)

ttk.Button(root, text="Generate", command = generate).pack()

root.mainloop()
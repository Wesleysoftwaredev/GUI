import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

def show_clock():
    label.pack(padx=20, pady=20)
    update_time()

root = tk.Tk()
root.title("Menu Clock")

menubar = tk.Menu(root)
root.config(menu=menubar)

clock_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Clock", menu=clock_menu)

clock_menu.add_command(label="Show Clock", command=show_clock)
label = tk.Label(root, font=("Helvetica", 48), bg= "black", fg = "cyan")

root.mainloop()
